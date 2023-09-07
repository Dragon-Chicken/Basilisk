#new branch
from sys import platform
import os
if platform == "linux" or platform == "linux2":
    # linux
    os.system("pip3 install -r requirements.txt")
elif platform == "darwin":
    # OS X
    os.system("pip3 install -r requirements.txt")
elif platform == "win32":
    os.system("pip install -r requirements.txt")