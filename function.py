#default function

def demo():
    print "welcome"
demo()

#defining the function with argument

def add(a,b):
    return a+b
#taking values from the user  
a=int(input("enter a"))
b=int(input("enter b"))
#calling a function
print("answer is",add(a,b))


#keyword argument function

def rect(l,b,h):
    return l*b
a=rect(b=6,l=4,h=2)
print(a)


#scope

#global variable

x=15
def change():
    global x
    x=x+5
    print("value of x inside the function",x)
change()
print("value of x inside the function",x)


#lambda function

def demo(n):
    return lambda a:a*n
b=demo(5)
c=demo(2)

print(b(2))
print(c(4))
