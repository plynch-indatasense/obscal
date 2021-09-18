# function to retrive calander entries
#def get_ical():
 #   f = open("icalout.txt", "r")
  #  return f

# get calander entries
#f = (get_ical())
#calstr = f.read()
f = open("icalout.txt", "r")
g = f.read()
print(g.find("•"))
print(g.find("•")+1)
#print(f(f.find("•")):(f.find("•"))+1)  

f.close







