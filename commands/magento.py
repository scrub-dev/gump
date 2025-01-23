import argparse
import itertools
import json
import utils
import utils.getFile
import subprocess

import utils.printer

def parseCommandType(x: str, commandList):
    y = str(x.split(' ')[0]).lower()
    if y == 'grunt':
        return commandList[1](x)
    elif y == 'composer':
        return commandList[2](x)
    else: return commandList[0](x)
    
def main(params: list) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=str)
    parser.add_argument("commands", type=str, nargs="*")
    args = parser.parse_args(params)

    with open(utils.getFile.config("conf.json", "magento")) as conf:
        conf = json.load(conf)

    def getSitePhpVer(site: str):
        if(site in conf["sites"]): return "php"+conf["sites"][site]["php_version"]
        else: return "php"+conf["sites"]["default"]["php_version"] 

    magentoCommand = lambda x: f"{conf['environments'][conf['magento_env']]} {getSitePhpVer(args.site)} {conf['magento_site_root']}{args.site}/{conf['magento_site_bin']} {x}"

    gruntCommand = lambda x:f"wsl exec bash -c 'export PATH=\"{conf['nvm_grunt_route']}:$PATH\"; grunt --gruntfile {conf['magento_site_root']}{args.site}/Gruntfile.js {x.split(' ')[1]}'" \
                            if conf["using_nvm"] \
                            else f"wsl -- grunt --gruntfile {conf['magento_site_root']}{args.site}/Gruntfile.js {x.split(' ')[1]}"
    composerCommand = lambda x:f"wsl exec bash -c 'cd {conf['magento_site_root']}{args.site};{getSitePhpVer(args.site)} /usr/local/bin/composer {x.split(' ')[1]}'"

    commandList = [magentoCommand, gruntCommand, composerCommand]


    args.commands = ' '.join(args.commands)
    if(args.commands == ""):
        try:
            print(conf["aliases"]["default"])
            utils.printer.console("No Commands providing, running default")
            args.commands = "default"
        except:
            utils.printer.console("Default Alias not found")
            utils.printer.console("Create a default alias or specific a command / list of commands")
            return
    

    commands = ([ parseCommandType(x, commandList)
        for x in [conf["commands"][x] for x in list(
            itertools.chain.from_iterable(
                e for e in [conf["aliases"][command].split(",")
                if command in conf["aliases"]
                else [command]
                for command in args.commands.split(",")]
            )) if x in conf["commands"]]])

    utils.printer.console(f"Site: {args.site}")
    utils.printer.console(f"Site Environment: {conf['magento_env']}")
    utils.printer.console(f"Site Location: {conf['magento_site_root']}{args.site}/")
    utils.printer.console("Command" + ('s' if len(commands) > 1 else ''))
    [utils.printer.console(c,2) for c in commands]
    print()
    [subprocess.call(command) for command in commands]
    print("\nDone!")
    return

def help():

    return