# gump password length [optional charsets / default A-Za-z0-9]
import argparse
from genericpath import isfile
from itertools import chain
import logging
from ntpath import join
import os

import utils.printer
import utils
import json
import subprocess

import utils.wsl
import utils.wsl.utils

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

    
    name = (aliases[args.workspace]['name'] if args.workspace in aliases else args.workspace).lower()

    win_dirsInLocation = lambda a: [{"name": f.lower(), "location" : f"{a['location']}\\{f}","env":a['env']} for f in os.listdir(a['location']) if not isfile(join(a['location'], f))]
    wsl_dirsInLocation = lambda a: [{"name": f.lower(), "location" : f"{a['location']}/{f}","env":a['env']} for f in utils.wsl.utils.listDirectories(a)]
    res = [result for result in list(chain.from_iterable([wsl_dirsInLocation(x) if (x['env'] == "wsl") else win_dirsInLocation(x) for x in conf["places_to_look"]])) if result['name'] == name]

    if(len(res)) == 0:
        print("Project not found")
        return
    else: res = res[0]

    def wsFileExist(p) -> bool | None:
        if(p['env'] == "win"): return f"{p['name']}.code-workspace" in [f for f in os.listdir(p['location'])]
        else: return f"{p['name']}.code-workspace" in utils.wsl.utils.listDirectoryContents(f"{p['location']}")

    def opener(a): return (f"{res['name']}.code-workspace") if wsFileExist(a) else ''

    commandToRun = \
        f"wsl -- {conf['wsl_code']} {res['location']}/{opener(res)}" \
        if res['env'] == "wsl" else \
        f"{conf['win_code']} {res['location']}\\{opener(res)}"
        
    utils.printer.console(f"Running Command:", 1)
    utils.printer.console(f"{commandToRun}", 2)
    subprocess.run(commandToRun, shell=True)

    return
def help() -> None:
    return
