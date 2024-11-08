# gump password length [optional charsets / default A-Za-z0-9]
import argparse
import random


#TODO: Implement Basic Secure String Password Generation
#TODO: Add options to generate passwords based on word length
#      --> Include sprinkling punctuation to increase entropy

def main(parameters) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--len', type=int, default=0)
    parser.add_argument('-c', '--chars', type=str)

    args = parser.parse_args(parameters)
    
    availableCharacters = produceValidCharString(args.chars)
    len_chars = len(availableCharacters)

    counter = 0
    length = args.len if args.len > 0 else 16
    output = ""
    while counter < length:
        output += availableCharacters[random.randrange(0, len_chars)]
        counter+=1
    print(f"Output:")
    print(f"{output}")

def help() -> None:
    print("Generates a password")
    print("Usage: password [length] -c/--characters=[Aa0!]")
    print("Character Examples: A=uppercase A-Z, a=lowercase a-z, 0=numbers 0 through 9, !=punctuation [!?/\#'@]")

def produceValidCharString(input: str) -> str:
    if input:
        validPasswordChars = ""
        if any(x.isupper() for x in input): validPasswordChars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if any(x.islower() for x in input): validPasswordChars += "abcdefghijklmnopqrstuvwxyz"
        if any(x.isdigit() for x in input): validPasswordChars += "0123456789"
        if not input.isalnum() : validPasswordChars += "!\"£$%^&*()#@\'/\\"
        return validPasswordChars
    else:
        return produceValidCharString("Aa0!")