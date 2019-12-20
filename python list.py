x=["python",".net","php","java","c++"]
print(x)

# to print the list values based on position
print(x[1])
print(x[-1])
print(x[1:2])
print(x[:2])
print(x[2:])
print(x[-2:-1])



# code for  change the item 
a=["python",".net","php","java","c++"]
a[2]="c"
print(a)


# code for  check if  item exist in list

a=["python",".net","php","java","c++"]
if "python" in a:
    print("true")

# find  length of list

a=["python",".net","php","java","c++"]
print(len(a))

# append  method to add a element

a=["python",".net","php","java","c++"]
a.append("c")
print(a)


#to  insert in particular position

a=["python",".net","php"]
a.insert(1,"c++")
print(a)

# remove  the value from list
a=["python",".net","php"]
a.remove(".net")
print(a)

# pop  --> remove the item in particular position
a=["python",".net","php"]
a.pop()
print(a)

#  delete the item in particular position
a=["python",".net","php"]
del  a[0]
print(a)


# clear  the list

#a=["python",".net","php"]
#a.clear()
#print(a)


# copy one list to another

 # a=["python",".net","php"]
# b= a.copy()
 #print(b)


# copy one list to another

a=["python",".net","php"]
b =list(a)
print(b)

# join two list 
a=["python",".net","php"]
b=["gg","hh"]
c=a+b
print(c)


# append -  add one list with another
a=["python",".net","php"]
b=["gg","hh"]
a.append(b)
print(a)


 # extend -  add one list with another
a=["python",".net","php"]
b=["gg","hh"]
a.extend(b)
print(a)


# to reverse the list values
a=["python",".net","php"]
a.reverse()
print(a)

# to sort the list values

a=["python",".net","php"]
a.sort()
print(a)


# to get the list values from user in list append

a=[]                                            # creating an empty list
n=int(input("enter the number of elements"))    # no of elements as input

for i in range(0,n):                            #iterating till the range
    b=int(input())
    a.append(b)                                 # adding the element 

print(a)  







