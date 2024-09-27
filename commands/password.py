# gump password length [optional charsets / default A-Za-z0-9]
import argparse

def main(parameters) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, required=True)
    parser.add_argument('-c', '--chars', type=str)

    args = parser.parse_args(parameters)

    print(args)

def help() -> None:
    print("Generates a password")
    print("Usage: password [length] -c/--characters=[Aa0!]")
    print("Character Examples: A=uppercase A-Z, a=lowercase a-z, 0=numbers 0 through 9, !=punctuation [!?/\#'@]")