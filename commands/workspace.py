# gump password length [optional charsets / default A-Za-z0-9]
import argparse
import logging

import utils.printer
logger: logging.Logger
import utils
import json
import subprocess

def main(parameters) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=str)
    args = parser.parse_args(parameters)

    with open(utils.getFile.config("conf.json", "workspace")) as conf:
        conf = json.load(conf)
    with open(utils.getFile.config("aliases.json", "workspace")) as aliases:
        aliases = json.load(aliases)["aliases"]

    workspaceLoc = f"{aliases[args.workspace] if args.workspace in aliases else args.workspace}"
    commandToRun = f"wsl -- {conf['vsc_loc']} {conf['base']}/{workspaceLoc}/{workspaceLoc}.code-workspace" if conf["env"] == "wsl" else f""
    utils.printer.console(f"Opening {workspaceLoc} workspace", 1)
    utils.printer.console(f"Running Command:", 1)
    utils.printer.console(f"{commandToRun}", 2)
    subprocess.run(commandToRun)

    # Update the command to accept aliases in different base locations, not just conf['base'] with locked env in wsl
    # check for a workspace file, if one does not exist, just open the folder in code
    return
def help() -> None:
    return
