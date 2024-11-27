# gump password length [optional charsets / default A-Za-z0-9]
import argparse
import logging

import utils.printer
logger: logging.Logger
import utils
import json
import subprocess

# Env var is not specifically where it is stored but how to access the workspace or work folder.
# IE: If it is on the L: Drive and you dont need to go through WSL, you would use WIN Env.
# All WSL-Core Core Sites will use WSL env. Most PHP/Magento sites will use WIN.

# TODO: Create a searcher that tries to find the workspace in either WSL or WIN and open it without needing to specify a environment location in aliases or use a default one in conf

def main(parameters) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=str)
    args = parser.parse_args(parameters)

    with open(utils.getFile.config("conf.json", "workspace")) as conf:
        conf = json.load(conf)
    with open(utils.getFile.config("aliases.json", "workspace")) as aliases:
        aliases = json.load(aliases)["aliases"]

    workspaceLoc = f"{aliases[args.workspace]['name'] if args.workspace in aliases else args.workspace}"
    workspaceEnv = aliases[args.workspace]['env'] if args.workspace in aliases else conf['default_env']

    commandToRun = f"wsl -- {conf['wsl_loc']} {conf['wsl_base']}/{workspaceLoc}/{workspaceLoc}.code-workspace" if workspaceEnv == "wsl" else \
        f"{conf['win_loc']} {conf['win_base']}\\{workspaceLoc}"
    
    utils.printer.console(f"Opening {workspaceLoc} workspace", 1)
    utils.printer.console(f"Running Command:", 1)
    utils.printer.console(f"{commandToRun}", 2)
    subprocess.run(commandToRun, shell=True)

    # Update the command to accept aliases in different base locations, not just conf['base'] with locked env in wsl
    # check for a workspace file, if one does not exist, just open the folder in code
    return
def help() -> None:
    return
