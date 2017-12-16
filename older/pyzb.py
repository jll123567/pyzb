import random
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
master=open("master.txt","w")
m=""
for i in range(0,1000):
    m=m+str(random.randint(0,1))
master.write(m*1000)
master.close()

master=open("master.txt","r")
r=master.read()
opt=input()
for i in range(int(opt)):
    f=open(str(random.randint(0,9999))+".txt","w")
    f.write(r)
    f.close()
master.close()