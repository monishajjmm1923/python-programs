
# get tuple values from user
a = tuple(input("Enter the tuple elements ..."))   
print(a) 
 
# print the item based on index value 
b = tuple(input("Enter the tuple elements ..."))  
print(b[1])


a=("a","b","c","d","e","f","g")
print(a[-1])
print(a[2:5])
print(a[-4:-1])


# print the values using for loop
a=("a","b","c","d","e","f","g")
for b in a:
    print(b)


# check specified item is present in a tuple use the in keyword
a=("a","b","c","d","e","f","g")
if "c" in a:
    print("true")

# tuple length
a=("a","b","c","d","e","f","g")
print(len(a))


# joint tuples
a = tuple(input("Enter the tuple elements ..."))   
b = tuple(input("Enter the tuple elements ..."))
c=a+b
print(c)


# to  returns the number of times a specified value appears in the tuple.
a=("a","b","b","d","b","f","b")
print(a.count("b"))

#Search for the first occurrence of the value "b", and return its position:
a=("a","b","b","d","b","f","b")
print(a.index("b"))

