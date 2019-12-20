import json

file=open("hello.json","r")
data=json.load(file)
print(data)
