# gump password length [optional charsets / default A-Za-z0-9]
import argparse
import json
import os
import utils
import utils.getFile
import utils.printer

def main(parameters) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('verb', type=str, choices=["edit", "show"])
    parser.add_argument('group_file', type=str)
    parser.add_argument('kv_pair', type=str)

    args = parser.parse_args(parameters)
    config_files = []

    print(utils.getFile.root())

    for path, subdirs, files in os.walk(os.path.join(utils.getFile.root(), "configs")):
        for name in files:
            if name.endswith('.json'):
                _path = os.path.join(path, name)
                _name = (path.split(os.path.join(utils.getFile.root()) + os.path.sep)[1] + os.path.sep + name.split(".")[0]).split(f"configs{os.path.sep}")[1]
                _json = json.load(open(_path))
                utils.printer.console("\033[1m===\033[0m" * 10)
                utils.printer.console(f"\033[1mConfig: {_name}\033[0m")
                utils.printer.console(f"Path: {_path}", 1)
                utils.printer.console("\033[1mContents:\033[0m", 1)
                getObjectDetails(_json, 1)
                config_files.append({"name": _name, "path": _path})

    # [print(conf) for conf in config_files]


def help() -> None:
    return



def getObjectDetails(obj, depth) -> None:
    for key, value in obj.items():
        if((type(value) == list) and len(value) > 1):
            utils.printer.console(f"{key}:", depth + 1)
            for item in value:
                if type(item) == dict:
                    utils.printer.console("-"*20,depth + 3)
                    getObjectDetails(item, depth + 2)
                else:
                    utils.printer.console(f"{item}", depth + 2)
        else:
            utils.printer.console(f"{key}: {value}",depth + 1)