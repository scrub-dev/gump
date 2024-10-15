import logging
import os
import utils.getFile

def getLogger() -> logging.Logger:
    createLogDir()
    logger = logging.getLogger("gump_logs")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(utils.getFile.log('errors'), mode='a+')
    handler.setLevel(logging.DEBUG)
    format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(format)
    logger.addHandler(handler)
    return logger

def getCommandLogger() -> logging.Logger:
    createLogDir()
    commandLogger = logging.getLogger("gump_commands")
    commandLogger.setLevel(logging.DEBUG)
    commandLogHandler = logging.FileHandler(utils.getFile.log('commands'), mode='a+')
    commandLogHandler.setLevel(logging.DEBUG)
    commandFormat = logging.Formatter('%(asctime)s - %(message)s')
    commandLogHandler.setFormatter(commandFormat)
    commandLogger.addHandler(commandLogHandler)
    return commandLogger


def createLogDir() -> None:
    if not os.path.exists(os.path.join(utils.getFile.root(), "logs")):
        os.mkdir(os.path.join(utils.getFile.root(), "logs"))