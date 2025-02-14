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

def main(parameters) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=str)
    args = parser.parse_args(parameters)

    with open(utils.getFile.config("conf.json", "workspace")) as conf:
        conf = json.load(conf)
    with open(utils.getFile.config("aliases.json", "workspace")) as aliases:
        aliases = json.load(aliases)["aliases"]

    
    name = (aliases[args.workspace]['name'] if args.workspace in aliases else args.workspace).lower()

    _win_dirsInLocation = lambda a: [{"name": f.lower(), "location" : f"{a['location']}\\{f}","env":a['env']} \
                                    for f in os.listdir(a['location']) if not isfile(join(a['location'], f))]
    
    _wsl_dirsInLocation = lambda a: [{"name": f.lower(), "location" : f"{a['location']}/{f}","env":a['env']} \
                                    for f in utils.wsl.utils.listDirectories(a)]
    
    def win_dirsInLocation(a):
        res = None
        try:
            res = _win_dirsInLocation(a);
        except:
            return []
        return res if len(res) > 0 else []
    def wsl_dirsInLocation(a):
        res = None
        try:
            res = _wsl_dirsInLocation(a);
        except:
            return []
        return res if len(res) > 0 else []
    
    res = [result for result in list(chain.from_iterable([wsl_dirsInLocation(x) if (x['env'] == "wsl") else win_dirsInLocation(x) \
                                                          for x in conf["places_to_look"]])) if result['name'] == name]

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
