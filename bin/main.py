# Import libraries
import pandas as pd
from lib import (fingerprint_features, fingerprint_array, preprocess,
                 get_features_target, train_and_evaluate, prediction)
from sklearn import svm
import argparse
import logging
log = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%I:%M:%S')


def main():
    df = pd.read_csv('dataset_single.csv')
    df = preprocess(df)

    X, y = get_features_target(df, 'P1')
    # MODELLING
    SVC_model = svm.SVC(kernel='rbf', gamma=100)
    train_and_evaluate(df, 'P1', SVC_model)

    # Predict P1 for any given smile
    parser = argparse.ArgumentParser(description='Enter smile')
    parser.add_argument('string', type=str, help='Enter word or words', nargs='*')
    args = parser.parse_args()
    smile = args.string[0]

    pred = prediction(smile, 'model.joblib')
    log.info(f"P1 = {pred}")


if __name__ == "__main__":
    main()
