#if condition
a=int(input("enter a"))
if(a%2==0):
    print("even")
else:
    print("odd")

# if with and
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if(a>b and a<c):                  #Both conditions are True
    print("true")
else:
    print("false")

# if with or
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if(a>b or a<c):                    #At least one of the conditions is True
    print("true")
else:
    print("false")

#elif statement
a=int(input("enter the mark"))
if a>85 and a<=100:
    print("A grade")
elif a>60 and a<=85:
    print("b grade")

elif a>40 and a<=60:
    print("c grade")
else:
    print("fail")