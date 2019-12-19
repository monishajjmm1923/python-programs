#without exception
a = int(input("Enter a:"))  
b = int(input("Enter b:"))  
c = a/b;  
print("a/b = %d"%c)  
  
#other code:  
print("welcome")  



#except statement with no exception

try:  
    a = int(input("Enter a:"))  
    b = int(input("Enter b:"))  
    c = a/b;  
    print("a/b = %d"%c)  
except:  
    print("false")  
else:  
    print("Hi I am else block")


 #this will throw an exception if the file doesn't exist. 
try:  
     fileptr = open("file.txt","r")  
except IOError:  
    print("File not found")  
else:  
    print("The file opened successfully")  
    fileptr.close() 



try:  
    fileptr = open("pip.py","r")     # block of code   
                                     # this may throw an exception  
    try:  
        fileptr.write("Hi I am good")  
    finally:  
        fileptr.close()  
        print("file closed")      # block of code  
                                 # this will always be executed 
except:  
    print("Error")


#To raise an value error exception
try:  
    age = int(input("Enter the age?"))  
    if age<18:  
        raise ValueError;  
    else:  
        print("the age is valid")  
except ValueError:  
    print("The age is not valid") 


#To raise an arithmetic error exception
try:  
    a = int(input("Enter a?"))  
    b = int(input("Enter b?"))  
    if b is 0:  
        raise ArithmeticError;  
    else:  
        print("a/b = ",a/b)  
except ArithmeticError:  
    print("The value of b can't be 0") 

