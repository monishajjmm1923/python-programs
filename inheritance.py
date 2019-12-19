#inheritance--->base class& derived class   A
#                                           |                                   
#single-level inheritance                   B
class demo1:                                           #base class declaration
    l=int(input("enter l"))
    b=int(input("enter b"))
    h=int(input("enter h"))
    def fun1(self):
        print("mul is",self.l*self.b*self.h)
class demo2(demo1):                                    #child class declaration
    def fun2(self):
        print("sum is",self.l+self.b+self.h)
obj=demo2()                                            #create a object for child class
obj.fun1()
obj.fun2()



#multi-level inheritance                     A
                                          #  |
class demo1:                              #  B           
    l=int(input("enter l"))               #  |
    b=int(input("enter b"))               #  C
    h=int(input("enter h"))
    def fun1(self):
        print("mul is",self.l*self.b*self.h)
class demo2(demo1):                                    
    def fun2(self):
        print("sum is",self.l+self.b+self.h)
class demo3(demo2):                                    
    def fun3(self):
        print("values are",self.l,self.b,self.h)

obj=demo3()                                          
obj.fun1()
obj.fun2()
obj.fun3()    

#                                            A    B
#multiple inheritance                           |                 
#                                               C                                          
class demo1:
    def sum(self,a,b):
        return a+b
class demo2:
    def sub(self,a,b):
        return a-b
class demo3(demo1,demo2):
    def mul(self,a,b):
        return a*b
obj=demo3()
print(obj.sum(19,23))
print(obj.sub(19,23))
print(obj.mul(19,23))
     
        
    