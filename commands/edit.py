# gump password length [optional charsets / default A-Za-z0-9]
import argparse

def main(parameters) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('group_file', type=str)
    parser.add_argument('kv_pair', type=str)

    args = parser.parse_args(parameters)

    print(args)


def help() -> None:
    return