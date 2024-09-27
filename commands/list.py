import os
import pathlib


def main() -> None:
    dir = pathlib.Path(__file__).parent.resolve()
    print("Commands Available:")
    [print(command.split(".")[0]) for command in os.listdir(dir) if os.path.isfile(os.path.join(dir, command))]

def help() -> None:
    print("Lists available commands")