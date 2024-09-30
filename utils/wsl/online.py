import subprocess
def check():
    out = subprocess.check_output("wsl -l -v | findstr * | /dev/null>1")
    print(out)