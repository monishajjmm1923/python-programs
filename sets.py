# display set values using for loop

a={"python",".net","c"}
print(a)
print(type(a))

for i in a:
    print(i)

#using set() method to print values
a=set(["python",".net","c"])
print(a)

#adding items to set
a={"python",".net","c"}
print("\n print original sets")
print(a)
print("\n adding other value to set")
a.add("php")
print(a)


#update method to add items
a=set(["python",".net","c"])
print("\n print original sets")
print(a)

a.update(["a","b"])
print("updated set",a)


#removing items from the set
a={"python",".net","c"}
a.discard("c")
for i  in a:
    print(i)


print("remove method")
a={"python",".net","c"}
a.remove("python")
print(a)

print("pop method")
a={"python",".net","c"}
a.pop()
print(a)


print("union method")
a={"a","b"}
b={"c","d"}
print(a.union(b))

print("intersection method")
a={"d","b"}
b={"c","d"}
print(a.intersection(b))

print("difference bw two set")
a={"d","b"}
b={"c","d"}
print(a-b)


#set comparison
a={"d","b"}
b={"c","d"}
print(a>b)
print(a<b)
print(a==b)







