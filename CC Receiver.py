import os
from pathlib import Path

FILEPATH = os.curdir + "\\files\\"
os.chdir(FILEPATH)


message = ""
paths = sorted(Path().iterdir(), key=os.path.getmtime)


for cf in paths:
    message = message + str(cf)[5]

print("message:" + message)

for filename in os.listdir(os.curdir):
        os.remove(os.curdir + "\\" + filename)
