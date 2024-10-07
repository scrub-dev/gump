import importlib.util
from types import ModuleType
import inspect
import utils
import utils.logging
import utils.logging.log

def load(source, modulename) -> ModuleType:
    spec = importlib.util.spec_from_file_location(modulename, source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run(module: ModuleType, parameters) -> None:

    if "main" in module.__dir__():

        setattr(module, "logger", utils.logging.log.getLogger())

        utils.logging.log.getCommandLogger().info(f"Command: {module.__name__} - Parameters: {parameters}")
        if len(inspect.getfullargspec(module.__getattribute__("main")).args) == 0: module.__getattribute__("main")()
        else: module.__getattribute__("main")(parameters)
    else:
        print("The " + module.__name__+ " command is missing its command entrypoint main() or could not be found...")
        print(module.__file__)

def getHelpDoc(module: ModuleType) -> None:
    if "help" in module.__dir__():
        module.__getattribute__("help")()
    
