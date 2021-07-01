# Import libraries
from lib import (prediction)
import argparse
import logging

log = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%I:%M:%S')


def main():
    # Predict P1 for any given smile
    parser = argparse.ArgumentParser(description='Enter smile')
    parser.add_argument('string', type=str, help='Enter word or words', nargs='*')
    args = parser.parse_args()
    smile = args.string[0]

    pred = prediction(smile, 'model.joblib')
    log.info(f"P1 = {pred}")


if __name__ == "__main__":
    try:
        main()
    except:
        log.info("Please run 'python bin/train_evaluate your-data' first")
