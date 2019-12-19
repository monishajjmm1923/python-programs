# creating class
class demo:
    x=input("enter name ")
a=demo()                           #calling  a class by creating instance
print(a.x)

#class with function
class demo:
    name=input("enter name")
    id=int(input("enter id"))
    def emp(self):
        print(self.name)
        print(self.id)
b=demo()                              #creatinga object
b.emp()                               #calling a function
        

# class with multiple function
class demo:
    name=input("enter name")
    id=int(input("enter id"))
    email=input("enter email")
    def emp1(self):
        print(self.name)
        print(self.id)
    def emp2(self):
        print(self.email)

b=demo()                               #creating a object
b.emp1() 
b.emp2()


#constructor--->__init__
#default constructor
class demo:
    def __init__(self):               #constructor will be automatically call
        print("welcome")
    def fun(self,name):
        print(name)
obj=demo()
obj.fun("mm")                         #call a function


#parameterized constructor
class demo:
    def __init__(self,name):
         print("stay positive")
         self.name=name
    def fun(self):
        print(self.name)
obj=demo("john")
obj.fun()


#In-built class functions
class demo1:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
s=demo1("jhon",101,22)

print(getattr(s,'name'))                       #prints the attribute name of the object s  

setattr(s,"age",23)                            # reset the value of attribute age to 23 

print(getattr(s,'age'))                         # prints the modified value of age 

print(hasattr(s,'id'))                          # prints true if the student contains the attribute with name id

#delattr(s,'age')                                # deletes the attribute age 

print(s.age)                                     # this will give an error since the attribute age has been deleted


#class attribute

class demo:
    "welcome"
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def fun(self):
        print(self.name,self.id)
s=demo("mm",23)
print(s.__doc__)                               #It contains a string which has the class documentation                   
print(s.__dict__)                              #It provides the dictionary 
print(s.__module__)                            #It is used to access the module in which, this class is defined.
print(s.__name__)                              #It is used to access the class name.                  
print(s.__bases__)                             #It contains a tuple including all base classes.
