import logging
import os
import utils.getFile

def getLogger() -> logging.Logger:
    logger = logging.getLogger("gump_logs")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(utils.getFile.log('errors'), mode='a+')
    handler.setLevel(logging.DEBUG)
    format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(format)
    logger.addHandler(handler)
    return logger

def getCommandLogger() -> logging.Logger:
    commandLogger = logging.getLogger("gump_commands")
    commandLogger.setLevel(logging.DEBUG)
    commandLogHandler = logging.FileHandler(utils.getFile.log('commands'), mode='a+')
    commandLogHandler.setLevel(logging.DEBUG)
    commandFormat = logging.Formatter('%(asctime)s - %(message)s')
    commandLogHandler.setFormatter(commandFormat)
    commandLogger.addHandler(commandLogHandler)
    return commandLogger