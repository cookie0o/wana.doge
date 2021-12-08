import ctypes
import os
import subprocess
import time
from subprocess import Popen

def main():
    try:
        #CHANGE BACKGROUND
        dirname = os.path.dirname(__file__)
        Background_path = os.path.join(dirname, 'res/rthtzjtzjtzjtzj.jpg')
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Background_path , 0)
        #OPEN UI
        dirname1 = os.path.dirname(__file__)
        UI = os.path.join(dirname1, 'UI.py')
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Background_path , 0)
        Popen(f'python {UI}')

    finally:
        pass

main()