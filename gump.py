import os
import pathlib
import sys
import json

import pyuac
import utils.createFiglet as figlet
import utils.loadModule as module
import utils.random

def main() -> None:
    printWelcomeMessage()
    command = []
    while (command == []):
        if len(sys.argv) == 1 :
            command = str(input("Command : ")).split()
            while (command == []):
                print("Press Ctrl+C or type exit to exit")
                command = str(input("Command : ")).split()
        else: command = sys.argv[1::]    
    if command[0].lower() == 'exit':
        print("Exiting...")
    else:
        run(command)
        print()

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

def run(commandArray) -> None:
    commandName = commandArray[0]
    commandPath = os.path.join(str(pathlib.Path(__file__).parent.resolve()),"commands", commandName + ".py")

    if os.path.isfile(commandPath) :
        command = module.load(commandPath, commandName)
        module.run(command, commandArray[1::])
    else:
        print("Could not find the command " + commandName)

if __name__ == "__main__":
    if not pyuac.admin.isUserAdmin():
        pyuac.admin.runAsAdmin()
    main()
