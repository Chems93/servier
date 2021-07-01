# Import libraries
import pandas as pd
from lib import (preprocess,
                 get_features_target, train_and_evaluate)
from sklearn import svm
import argparse
import logging
log = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%I:%M:%S')


def main():
    parser = argparse.ArgumentParser(description='Enter dataset name')
    parser.add_argument('string', type=str, help='Enter word or words', nargs='*')
    args = parser.parse_args()
    dataset = args.string[0]
    df = pd.read_csv(dataset)
    df = preprocess(df)

    X, y = get_features_target(df, 'P1')
    # MODELLING
    SVC_model = svm.SVC(kernel='rbf', gamma=100)
    train_and_evaluate(df, 'P1', SVC_model)


if __name__ == "__main__":
    main()
