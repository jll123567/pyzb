import random
import time
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jledbetter2019
#
# Created:     04/11/2016
# Copyright:   (c) jledbetter2019 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
master=open("master.txt","r")
r=master.read()
for i in range(1):
    f=open(str(random.randint(0,9999))+".txt","w")
    f.write(r)
    f.close()
master.close()

