import os
import pathlib
import sys
import json

import pyuac

import utils.createFiglet as figlet
import utils.module
import utils.module.checkModulePermission
import utils.module.loadModule as module
import utils.random
import utils.wsl
import utils.wsl.instance
import utils.wsl.online

def main(parameters) -> None:
    if parameters[0].lower() == 'exit':
        print("Exiting...")
    else:
        run(command)
        print()

@pyuac.main_requires_admin(return_output=True)
def main_with_admin(parameters) -> None:
    main(parameters)

def getCommand(parameters) -> list[str]:
    command = []
    while (command == []):
        if len(parameters) == 1 :
            command = str(input("Command : ")).split()
            while (command == []):
                print("Press Ctrl+C or type exit to exit")
                command = str(input("Command : ")).split()
        else: command = parameters[1::] 
    return command   

def printWelcomeMessage () -> None:
    conf = json.load(open("./configs/conf.json"))
    print(figlet.create(conf['NAME'].upper()) + "v" + conf["VERSION"])
    print ("~" * len(conf['DESC']))
    print(conf['DESC'])

    with open("./configs/motds.json") as motds:
        motds = json.load(motds)
        motd = utils.random.array(motds['hints'])
        print(motd)

    print ("~" * len(conf['DESC']))

def getCommandPath(commandName) -> str:
    return os.path.join(str(pathlib.Path(__file__).parent.resolve()),"commands", commandName + ".py")

def run(commandArray) -> None:
    commandPath = getCommandPath(commandArray[0])

    if os.path.isfile(commandPath) :
        command = module.load(commandPath, commandArray[0])
        module.run(command, commandArray[1::])
    else:
        print("Could not find the command " + commandArray[0])

if __name__ == "__main__":
    printWelcomeMessage()
    command = getCommand(sys.argv)
    if utils.module.checkModulePermission.requireAdmin(getCommandPath(command[0]), command[0]): main_with_admin(command)
    else: main(command)