#def wesh():
 #   print("hello world!")

import pandasss as pd
from lib import fingerprint_features, fingerprint_array
from sklearn.model_selection import train_test_split
from sklearn import svm
import argparse
from sklearn.metrics import classification_report




def wesh():
    #from lib import fingerprint_features, fingerprint_array
    df = pd.read_csv('dataset_single.csv')

    # DATA PRE PROCESSING
    # Extract features from smiles
    df['fingerprint'] = df['smiles'].apply(lambda x: fingerprint_features(x))
    # Transform fingerprint to array
    df['fp'] = df['fingerprint'].apply(lambda x: fingerprint_array(x))
    # Create dummy variable for each molecule property
    df[list(range(2048))] = pd.DataFrame(df.fp.values.tolist(), index=df.index)
    # Classes are highly unbalanced, we'll oversample the minority class
    pos = df[df['P1'] == 1]
    pos = pos.sample(n=round(len(df) * 0.6), replace=False)
    neg = df[df['P1'] == 0]
    neg = neg.sample(n=round(len(df) * 0.4), replace=True)
    df = pos.append(neg, ignore_index=True)
    # Create X (features) and y (output) datasets
    X = df.drop(['mol_id', 'smiles', 'fingerprint', 'fp', 'P1'], axis=1)
    y = df['P1']
    # MODELLING
    # Create train and test dataset, given the number of observation we won't split the data in train/test/validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3,
                                                        random_state=100)
    # Fit the Support Vector Model
    SVC_model = svm.SVC(kernel='rbf', gamma=100).fit(X_train, y_train)
    # Predict
    SVC_prediction = SVC_model.predict(X_test)
    # Evaluate the model
    #print(classification_report(SVC_prediction, y_test))
    parser = argparse.ArgumentParser(description='Enter string')
    parser.add_argument('string', type=str, help='Enter word or words', nargs='*')
    args = parser.parse_args()
    print(args.string[0])
    #print(str(nadir))


if __name__ == "__main__":
    wesh()
