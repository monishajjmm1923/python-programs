#to print values
a={"name":"mm", "id":23}
print(type(a))
print(a)
print("employee data")
print("name: %s"%a["name"])   
print("id: %s" %a["id"])

#updating dictionary values
a={"name":"mm", "id":23}
print("before updating",a)
print("enter the new values")
a["name"]=input("name")           #get name from user
a["id"]=input("id")               #get id from user
print(a)

# delete dictionary values
a={"name":"mm", "id":23}
print("before deleting",a)
del a["name"]
print("after deleting",a)

#for loop to print all the keys of a dictionary
a={"name":"mm", "id":23}
for i in a:
    print(i)

#for loop to print the values of the dictionary by using values() method.
a={"name":"mm", "id":23}
for i in a.values():
    print(i)

#for loop to print the items of the dictionary by using items() method.
a={"name":"mm", "id":23}
for i in a.items():
    print(i)

#nested dictionary

a={
    "a1":{"name":"mm", "id":23},
    "a2":{"name":"jj", "id":19},
    "a3":{"name":"mj", "id":23}
}
print(a)


#clear dictionary
b={}                              #declaring b
b["name"]=input("name")           #get name from user
b["id"]=input("id")  
print("before clearing",b)
b.clear()
print("after clearing",b)

#copy dictionary
a={"name":"mm", "id":23}
b=a.copy()
print(b)

#Get the value of the "model" item
a={"name":"mm", "id":23}
b=a.get("id")
print(b)

#Removes the element with the specified key
a={"name":"mm", "id":23}
a.pop("id")
print(a)

#Removes the last inserted key-value pair
a={"name":"mm", "id":23,"dob":"ruru"}
a.popitem()
print(a)