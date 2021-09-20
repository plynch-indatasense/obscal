# function to retrive calander entries
import os

# If file does not exist catch error
try:
    os.remove("/Users/pblynch/.calout/cal.md")
except:
    print ("no file")


def writeout(output):
    w = open("/Users/pblynch/.calout/cal.md", "a")
    w.write(output)
    w.close()

f = open("icalout.txt", "r")
g = f.read()
new = (g.split("•"))
for x in new:
    temp = x.splitlines()
    if (len(temp)>0):
        writeout("##### " + temp[0] + " #####" + "\n")
        writeout( temp[2] + "\n")
        writeout("##### " + temp[2] + " #####" + "\n")









f.close






