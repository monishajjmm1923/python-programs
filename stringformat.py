#The format() method allows you to format selected parts of a string.
name=input("enter name")
txt="welcome {} have a nice day"
print(txt.format(name))

# for decimal value
price = int(input("enter"))
txt = "The price is {:.2f} dollars"
print(txt.format(price))

#add more placeholders:
name=input("enter name")
id=int(input("enter id"))
salary=float(input("enter salary"))
txt=" name is {} id is {} salary is{}"
print(txt.format(name,id,salary))


# use the index number
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

