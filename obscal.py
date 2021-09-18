# function to retrive calander entries
import os
#os.remove("/Users/plynch/Code/obscal/obscal/cal.md")


def writeout(output):
    w = open("cal.md", "a")
    w.write(output)
    w.close()



f = open("icalout.txt", "r")
g = f.read()
new = (g.split("•"))
for x in new:
    temp = x.splitlines()
    print(temp)
    writeout("##### " + temp[1] + " #####" + "\n")
    writeout( temp[2] + "\n")
    writeout("##### " + temp[3] + " #####" + "\n")

f.close 








