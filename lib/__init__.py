from rdkit.Chem import rdMolDescriptors, MolFromSmiles, rdmolfiles, rdmolops, DataStructs
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import logging as log
from sklearn.metrics import classification_report
from joblib import dump, load


def fingerprint_features(smile_string, radius=2, size=2048):
    mol = MolFromSmiles(smile_string)
    new_order = rdmolfiles.CanonicalRankAtoms(mol)
    mol = rdmolops.RenumberAtoms(mol, new_order)
    return rdMolDescriptors.GetMorganFingerprintAsBitVect(mol, radius,
                                                          nBits=size,
                                                          useChirality=True,
                                                          useBondTypes=True,
                                                          useFeatures=False
                                                          )


def fingerprint_array(fp):
    """
    This function transform a rdkit vector in array
    """
    arr = np.zeros((0,), dtype=np.int8)
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr


def adjusted_classes(y_pred, t):
    """
    This function adjusts class predictions based on the prediction threshold (t).
    Will only work for binary classification problems.
    """
    return [1 if y >= t else 0 for y in y_pred]


def extract_features_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract features from smile and convert them to array.
    """
    df['fingerprint'] = df['smiles'].apply(lambda x: fingerprint_features(x))
    df['fp'] = df['fingerprint'].apply(lambda x: fingerprint_array(x))
    return df


def create_dummies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create as many dummy variables as features
    """
    df[list(range(len(df['fp'][0])))] = pd.DataFrame(df.fp.values.tolist(), index=df.index)
    return df


def oversampling(df: pd.DataFrame) -> pd.DataFrame:
    """
    The minority class needs to be oversampled when the data is unbalanced.
    Create minority and majority datasets and draw with replacement 40% of the minority class and draw without
    replacement 60% of the majority class to build a new balanced dataset.
    """
    majority = df[df['P1'] == 1]
    majority = majority.sample(n=round(len(df) * 0.6), replace=False)
    minority = df[df['P1'] == 0]
    minority = minority.sample(n=round(len(df) * 0.4), replace=True)
    df = majority.append(minority, ignore_index=True)
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Call all the preprocessing function above.
    """
    df = extract_features_df(df)
    df = create_dummies(df)
    df = oversampling(df)
    return df


def get_features_target(df: pd.DataFrame, target_variable):
    """
    Create features and output datasets
    """
    features = df.loc[:, [col for col in df.columns if col != target_variable]]
    features = features.drop(['mol_id', 'smiles', 'fingerprint', 'fp'], axis=1)
    target = df.loc[:, [target_variable]]
    return features, target


def train_and_evaluate(df, target_variable, model):
    """
    Train and evaluate the model
    """
    X, y = get_features_target(df, target_variable)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3,
                                                        random_state=100)
    model.fit(X_train, y_train.values.ravel())

    prediction = model.predict(X_test)
    log.info(f"Model Performance: {classification_report(prediction, y_test)} ")

    dump(model, 'model.joblib')


def prediction(smile, model):
    saved_model = load(model)
    return saved_model.predict(fingerprint_array(fingerprint_features(smile)).reshape(1, -1))[0]




