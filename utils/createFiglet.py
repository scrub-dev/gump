import pyfiglet

def create(str, font = "", width = 100) -> str:
    if(font != ""): return pyfiglet.figlet_format(str, font)
    else: return pyfiglet.figlet_format(str, font = "slant", width= width)