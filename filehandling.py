#open a file
fileptr = open("file.py","r")  
  
if fileptr:  
    print("file is opened successfully") 
    

#To read a file using fileobj.read(<count>)

fileptr = open("file.py","r"); 

a = fileptr.read(9);
print(a)

#stores all the data of the file into the variable content  
content = fileptr.readline();   
  
# prints the type of the data stored in the file  
print(type(content))   
  
#prints the content of the file  
print(content)   
  
#closes the opened file  
fileptr.close()


 #read the whole file.
a = open("file.py","r");   
  
#running a for loop   
for i in a:  
    print(i) # i contains each line of the file 



#add data in to the file
fileptr = open("file.py","a");   
  
#appending the content to the file  
fileptr.write("Python is the modern day language. It makes things so simple.")  
  
  
#closing the opened file   
fileptr.close()


#Using with statement
with open("pip.py",'r') as f:  
    content = f.read();  
    print(content) 



# open the file  in read mode  
fileptr = open("file.py","r")  
  
#initially the filepointer is at 0   
print("The filepointer is at byte :",fileptr.tell())  
  
#reading the content of the file  
content = fileptr.read();  
  
#after the read operation file pointer modifies. tell() returns the location   
  
print("After reading, the filepointer is at:",fileptr.tell())


#renaming the file

import os;  
  
#rename file2.txt to file3.txt  
os.rename("file2.txt","file3.txt")  


import os;  
  
#deleting the file named file3.txt   
os.remove("file3.txt")


import os;  
  
#printing the current working directory   
print(os.getcwd())  

