#print multiplication table using for loop

a=int(input("enter the table"))
for i in range(1,11):
    print("%dx%d= %d" %(a,i,a*i))

#while loop
i=1
while i<10:
    print(i)
    i+=1

#break stmt

i=1
while i<10:
    print(i)
    if i==2:
        break
    i += 1

#continue stmt
for a in "python":
    if a=="h":
        continue
    print(a)

#pass stmt

for a in [1,2,3,4,5]:
    if a==2:
        pass
    print a





