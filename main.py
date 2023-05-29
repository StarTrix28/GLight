import time
from tkinter import *
from pathlib import Path
import sys
import re
from Light import Array
from ast import literal_eval
Lines = []
variables = {}

my_file = Path("main.glt")
try:
    my_abs_path = my_file.resolve(strict=True)
except FileNotFoundError:
    print("FileNotFoundError")
    f = open("main.glt", "x")

    print("File has been created")
    sys.exit()
else:
    def window(title="GLight"):
        global canvas, root
        root = Tk()
        root.wm_title(title)
        canvas = Canvas(root)


    def line(pos=(0, 0), x2=0, z2="omgweird"):
        global canvas, Lines
        if z2 == "omgweird":
            z2 = pos[1]
        Lines = canvas.create_line(pos[0], pos[1], x2, z2)

    def getvar(name):
        global variables
        print(variables)
        return variables.get(name)
    def printL(var):
        global variables
        print(var)
    def wait(s=1):
        time.sleep(s)
    def math(a):
        return a
    def Main():
        global root, canvas, variables
        f = open("main.glt", "r+")
        s1 = re.split(";+", f.read(-1))
        lineExe = 0
        while lineExe != s1.index:
            cmd = s1[lineExe]
            if "window" in cmd:
                exec(cmd)
            elif "run" in cmd:
                canvas.pack(fill=BOTH, expand=1)
                root.mainloop()
            elif "end" in cmd:
                exec(exit())
            elif "line" in cmd:
                exec(cmd)
            elif "var" in cmd and not("getvar" in cmd):

                before_keyword, keyword, after_keyword = cmd.partition("var")
                _a = after_keyword.split("=")
                _a1 = _a[0]
                _a2 = _a[1]
                variables[_a1.replace(" ", "")] = _a2
            elif "getvar" in cmd:
                exec(cmd)
            elif "printL" in cmd:
                exec(cmd)
            elif "wait" in cmd:
                exec(cmd)
            elif "goto":
                before_keyword, keyword, after_keyword = cmd.partition("goto")
                lineExe = int(after_keyword)
            else:
                return True

            try:
                lineExe += 1
            except IndexError:
                sys.exit()




    pass

Main()
