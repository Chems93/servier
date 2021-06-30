from rdkit.Chem import rdMolDescriptors, MolFromSmiles, rdmolfiles, rdmolops, DataStructs
import numpy as np

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

