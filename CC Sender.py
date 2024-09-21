# Nikhil Patil
# CSEC 751
# Covert Channel Example

import os, random, time

FILEPATH = os.curdir + "\\files\\"

message = "i love you!!!!!!!!!!"

os.chdir(FILEPATH)

for char in message:
    filename = "file_" + char + "_" + str(random.randint(1,1000))
    f = open(filename, "w")
    f.close()
    time.sleep(2)

