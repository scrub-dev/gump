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

    # get env, if env wsl
    # utils.wsl.online.check
    # if false short circuit and return error.
    #TODO: Add safety check to see if WSL is alive if WSL is env.
    #TODO: Check if site is a valid site. or error gracefully
    #TODO: Manage Grunt Implementation


    #{conf['environments'][conf['magento_env']]}
    # if str(args.commands).lower() == 'grunt':
    #     commands = ([f"wsl exec --gruntfile {conf['magento_site_root']}{args.site}/Gruntfile.js {x.split(' ')[1]}" 
    #     for x in [conf["commands"][x] for x in list(
    #         itertools.chain.from_iterable(
    #             e for e in [conf["aliases"][command].split(",") 
    #             if command in conf["aliases"] 
    #             else [command] 
    #             for command in args.commands.split(",")]
    #         )) if x in conf["commands"]]])
        
    #     print(commands)
    #     return

    # removes invalid commands, checks for aliases first, creates a flat array of all command shorthands,
    # alias refers to shorthand, not full commands
    # making everything a single nested list comprehension if possible because... its still more readable than magento code...


    #TODO: Change grunt from a hard conf value to a lookup when command is ran ie: whereis grunt


    magentoCommand = lambda x: f"{conf['environments'][conf['magento_env']]} {conf['magento_site_root']}{args.site}/{conf['magento_site_bin']} {x}"
    gruntCommand = lambda x: f"wsl exec {conf['grunt_route']} --gruntfile {conf['magento_site_root']}{args.site}/Gruntfile.js {x.split(' ')[1]}"

    commands = ([(magentoCommand(x) if str(x.split(' ')[0]).lower() != 'grunt' else gruntCommand(x))
        for x in [conf["commands"][x] for x in list(
            itertools.chain.from_iterable(
                e for e in [conf["aliases"][command].split(",") 
                if command in conf["aliases"] 
                else [command] 
                for command in args.commands.split(",")]
            )) if x in conf["commands"]]])
    # print(commands)#

    utils.printer.console(f"Site: {args.site}")
    utils.printer.console(f"Site Environment: {conf['magento_env']}")
    utils.printer.console(f"Site Location: {conf['magento_site_root']}{args.site}/")
    utils.printer.console("Command" + ('s' if len(commands) > 1 else ''))
    [utils.printer.console(c,2) for c in commands]
    print()    
    # subprocess.call(commands)

    [subprocess.call(command) for command in commands]


    print("\nDone!")

    return

def help():

    return 