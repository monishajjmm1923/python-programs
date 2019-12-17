
a=10
print(type(a))
print(type("mm"))
print(type(34.9))
print(type(1+5j))


n=["mm","jj"]
print(type(n))


b=("mm","jj")
print(type(b))

c={"name":"jj"}
print(type(c))


d={"gg",56}
print(type(d))

e= frozenset({"a",45})
print(type(e))


print(type(True))
print(type(False))


f= b"mm"
print(type(f))




#############  numbers  #############
print(type(-35))
print(type(23e6))


#########  conversion  #########
a=float(5)
b=int(67.89)
c=complex(10)

print(a)
print(b)
print(c)


########### random number  ################

import random
print(random.randrange(1,10))



############## casting ############
print(int(2.5))
print(int("8"))

print(float("99"))
print(float(7))