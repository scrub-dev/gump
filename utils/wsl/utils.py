import utils.wsl
import utils.wsl.instance


def listDirectories(a) -> list:
    return [x for x in utils.wsl.instance.run(f"ls {a['location']}").split("\n") if x != '']

def listDirectoryContents(a) -> list:
    return [x for x in utils.wsl.instance.run(f"cd {a} && ls").split("\n") if x != '']