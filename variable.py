a=19
b="mm"
print(a)
print(b)

#############################

x,y,z="mm","jj","mj"
print(x)
print(y)
print(z)

####################################

x=y=z="welcome"
print(x)
print(y)
print(z)


##################################


a="moni"

print(a+"sha")


############## variable with function  ####################

a="awesome"
def abc():
    print("python is" +a)

abc()


############global###########

x="awesome"
def abc():
    global x
    x="fantastic"
abc()
print("python is"+x)


