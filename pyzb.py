# import
import random

# runtime
check = open("0.dll", "w")
check.close()
for i in range(1000):
    check = open("0.dll", 'r')
    master = open("master.dll", "r")
    fName = str(random.randint(0, 99999999999999999))
    f = open(fName+".dll", 'w')
    f.close()
    f = open(fName+".dll", "r")
    if f.read(1) != check.read(1):
        f.close()
    else:
        f.close()
        with open(fName+".dll", "w") as f:
            f.write(master.read())
    master.close()
    check.close()
