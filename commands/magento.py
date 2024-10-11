import argparse
import itertools
import json
import utils
import utils.getFile
import subprocess

import utils.printer
#bin/magento s:up && bin/magento setup:di:compile && bin/magento setup:static-content:deploy -f && bin/magento c:f 

def main(params: list) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=str)
    parser.add_argument("commands", type=str)
    args = parser.parse_args(params)

    with open(utils.getFile.config("conf.json", "magento")) as conf:
        conf = json.load(conf)

    # removes invalid commands, checks for aliases first, creates a flat array of all command shorthands,
    # alias refers to shorthand, not full commands
    # making everything a single nested list comprehension if possible because... its still more readable than magento code...
    commands = ([f"{conf['environments'][conf['magento_env']]} {conf['magento_site_root']}{args.site}/{conf['magento_site_bin']} {x}" 
        for x in list(set([conf["commands"][x] for x in list(
            itertools.chain.from_iterable(
                e for e in [conf["aliases"][command].split(",") 
                if command in conf["aliases"] 
                else [command] 
                for command in args.commands.split(",")]
            )) if x in conf["commands"]]))])
    # print(commands)#

    utils.printer.console(f"Site: {args.site}")
    utils.printer.console(f"Site Environment: {conf['magento_env']}")
    utils.printer.console(f"Site Location: {conf['magento_site_root']}{args.site}/")
    utils.printer.console("Command" + ('s' if len(commands) > 1 else ''))
    [utils.printer.console(c,2) for c in commands]
    print()    
    # subprocess.call(commands)

    [subprocess.call(command) for command in commands]


    print("Done!")

    return

def help():

    return 