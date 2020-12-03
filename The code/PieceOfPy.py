"""
  Copyright 2020 EagleOnGitHub, ProtoUncreative
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
        !!NOTICE!!
Changing the filename will
make the file to not properly
function. Please do not change the
filename from "PieceOfPy.py" to anything
else.
~Thanks!
"""
import math
import time
import sys
import os
terminateProgram = False
y=0
for x in os.listdir('./'):
    if x!='PieceOfPy.py':
        y+=1
    if y==len(os.listdir('./')):
        terminateProgram=True

if terminateProgram:
    print("Not in correct environment for proper work, ABORTING!")
    breakpoint("Intentional program killer.")

args = list()
argContinue = True

while argContinue:
    UI = input("Commands(Send empty line to stop):")
    if UI=='':
        argContinue=False
    else:
        args.append(UI)
filename = input("Filename(Spaces will be removed):")+'.c'.strip(' ')
file = open(filename, 'wb')
timerStart = int(round(time.time()*1000))
print("Processing..")
fin = ''
fin+='#include <stdio.h>\n\nint main() {\n'
for line in args:

    tempArgs0 = line.split(' ')
    temp0 = list(tempArgs0)
    stringTemp0 = ''
    tempArgs0.pop(0)
    for x in tempArgs0:
        stringTemp0+='%s ' % (x)
    stringTemp0 = stringTemp0[:-1]
    if len(stringTemp0) >= 5:
        if stringTemp0[:4]=="!num":
            stringTemp0 = stringTemp0[4:]
    for c in temp0:
        if c=="print":
            fin+="\tprintf("
            for c in tempArgs0:
                if c[:4]=="!num":
                    fin+='"%d",'
            fin+='"%s\\n"' % (stringTemp0)
            fin+=");\n"
fin+='\tsystem("pause");\n\treturn 0;\n'
fin+='}'
print("Writing..")
try:
    file.write(fin.encode(encoding=sys.getfilesystemencoding()))
except:
    print("Failure on printing! ABORT!")
    file.close()
    breakpoint("Intentional program killer.")
file.close()
print("File printed!")
print("Finished in: ~%ims" % (int(round(time.time()*1000))-timerStart))
#print("The code: %s" % (fin)) #debug purposes only
_ = input("")