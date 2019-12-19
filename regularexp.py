import re
str = input("enter u r name") 
  
matches = re.findall("m", str)     #This method returns a list containing a list of all matches
print(matches) 


b = re.search("o", str)            #return how many matches occur
print(b) 
print(b.span())                    #return position