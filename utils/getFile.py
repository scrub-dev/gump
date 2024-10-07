import os


def config(name, dir = "") -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), *["..","configs", *dir.split("/"), name])

def log(name) -> str:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), *["..","logs", f"{name}.log"])
