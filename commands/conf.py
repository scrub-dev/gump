# gump password length [optional charsets / default A-Za-z0-9]
import argparse
import json
import os
import re
import utils
import utils.getFile
import utils.printer

def main(parameters) -> None:
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='verb', help='sub-command help', required=True)


    parser_show = subparsers.add_parser('show', help='Show all configs')
    parser_show.add_argument('-a', '--all', action='store_true', help='List available configs')
    parser_show.add_argument('-v','--verbose', action='store_true', help='Show all config values')
    parser_show.add_argument('args', nargs='*')

    parser_edit = subparsers.add_parser('edit', help='Edit a config')
    parser_edit.add_argument('config', type=str, help='Config to edit', default="")
    parser_edit.add_argument('keyvalue', type=str, help='Key to edit (key:newvalue)', default="")

    args = parser.parse_args(parameters)

    if args.verb == "show":
        if args.all:
            listAllConfigs(verbose=args.verbose)
        elif args.args:
            findConfig(args.args[0])
        # return listAllConfigs()
        else:
            return parser_show.print_help()
    elif args.verb == "edit":

        return parser_edit.print_help()
    # [print(conf) for conf in config_files]

def help() -> None:
    return


def findConfig(name) -> None:
    _path = os.path.join(utils.getFile.root(), "configs", name.replace("/", os.path.sep).replace("\\", os.path.sep) + ".json")
    if os.path.exists(_path):
        _json = json.load(open(_path))
        utils.printer.console("\033[1m===\033[0m" * 10)
        utils.printer.console(f"\033[1mConfig: {name}\033[0m")
        utils.printer.console(f"Path: {_path}", 1)
        utils.printer.console("\033[1mContents:\033[0m", 1)
        getObjectDetails(_json, 1)

    return


def listAllConfigs(verbose: bool) -> None:
    config_files = []
    for path, subdirs, files in os.walk(os.path.join(utils.getFile.root(), "configs")):
        for name in files:
            if name.endswith('.json'):
                _path = os.path.join(path, name)
                _name = (path.split(os.path.join(utils.getFile.root()) + os.path.sep)[1] + os.path.sep + name.split(".")[0]).split(f"configs{os.path.sep}")[1]
                _json = json.load(open(_path))
                utils.printer.console("\033[1m===\033[0m" * 10)
                utils.printer.console(f"\033[1mConfig: {_name}\033[0m")
                utils.printer.console(f"Path: {_path}", 1)
                if verbose:
                    utils.printer.console("\033[1mContents:\033[0m", 1)
                    getObjectDetails(_json, 1)
                config_files.append({"name": _name, "path": _path})
    return


def getObjectDetails(obj, depth) -> None:
    for key, value in obj.items():
        if((type(value) == list) and len(value) > 1):
            utils.printer.console(f"{key}:", depth + 1)
            for item in value:
                if type(item) == dict:
                    utils.printer.console("~"*20,depth + 3)
                    getObjectDetails(item, depth + 2)
                else:
                    utils.printer.console(f"{item}", depth + 2)
        else:
            utils.printer.console(f"{key}: {value}",depth + 1)