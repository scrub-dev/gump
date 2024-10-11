import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--overwrite', type=str, required=False)
    parser.add_argument('-m','--minor', action='store_true')
    parser.add_argument('-mm','--major', action='store_true')
    parser.add_argument('-p', '--patch', action='store_true')

    args = parser.parse_args()
    print(args)