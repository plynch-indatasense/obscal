# function to retrive calander entries
import os
import datetime
# If file does not exist catch error
#try:
 #   os.remove("/Users/pblynch/.calout/cal.md")
#except:
 #   print ("no file")

#def writeout(output):
 #   w = open("/Users/pblynch/.calout/cal.md", "a")
  #  w.write(output)
   # w.close()

def newDayTemplate(data):
    tmp = open("/Users/pblynch/Documents/Obsidian/aws/dailyNotes/template.md", "r")
    tail = tmp.read()
    today = datetime.datetime.now()
    outfile = open("/Users/pblynch/Documents/Obsidian/aws/dailyNotes/" + today.strftime("%Y-%m-%d") +  ".md","x") 
    outfile.write("# " + today.strftime("%A %d %b %Y")+ "\n")
    outfile.write("## Today \n")
    outfile.write(data)
    outfile.write(tail)
    outfile.close
    tmp.close

f = open("/Users/pblynch/.calout/icalout.txt", "r")
g = f.read()
new = (g.split("•"))
out = ""
for x in new:
    temp = x.splitlines()
    if (len(temp) > 0): 
        temp[0] = "```\n"+ temp[0]+ "\n"
        temp[-1] = "\n" + temp[-1] + "\n ```\n"
        #temp[0] = "##### " + temp[0] + "\n"
        #temp[-1] ="\n###### " + temp[-1] +"\n"
        for y in temp:
            print (y)
            out = out + y

print(out)

newDayTemplate (out)  







f.close






