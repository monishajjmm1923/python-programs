#iterator
x=("c","c++","python")
y=iter(x)

print(next(y))
print(next(y))
print(next(y))


#To create an object/class as an iterator 
# to implement the methods __iter__() and __next__() to your object.

class Test: 
  
    # Cosntructor 
    def __init__(self, limit): 
        self.limit = limit 
  
    # Called when iteration is initialized 
    def __iter__(self): 
        self.x = 10
        return self
  
    # To move to next element. In Python 3, 
    # we should replace next with __next__ 
    def next(self): 
  
        # Store current value ofx 
        x = self.x 
  
        # Stop iteration if limit is reached 
        if x > self.limit: 
            raise StopIteration 
  
        # Else increment and return old value 
        self.x = x + 1; 
        return x 
  
# Prints numbers from 10 to 15 
for i in Test(15): 
    print(i) 
  
