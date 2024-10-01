from utils.module import loadModule

def requireAdmin(commandPath, commandName):
    module = loadModule.load(commandPath, commandName)
    if hasattr(module, "REQUIRE_ADMIN"):
        return module.__getattribute__("REQUIRE_ADMIN")
    else: return False