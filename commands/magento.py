import argparse
import itertools
import json
import utils
import utils.getFile
#bin/magento s:up && bin/magento setup:di:compile && bin/magento setup:static-content:deploy -f && bin/magento c:f 
REQUIRE_ADMIN = True

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
    commands = " && ".join([f"{conf['environments'][conf['magento_env']]} {conf['magento_site_root']}{args.site}/{conf['magento_site_bin']} {x}" 
        for x in list(set([conf["commands"][x] for x in list(
            itertools.chain.from_iterable(
                e for e in [conf["aliases"][command].split(",") 
                if command in conf["aliases"] 
                else [command] 
                for command in args.commands.split(",")]
            )) if x in conf["commands"]]))])
    

    print(commands)
    # execute command

    return

def help():

    return 