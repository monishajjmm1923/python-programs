#list

Officelist=["employees","computers","electronic items"]
mylist=[]
mylist=Officelist[:]
print(mylist)
print("getting elements by its index num: ",Officelist[1])
print("negative index: ",Officelist[-2])
print("range of index: ",Officelist[1:3])
Officelist[0]="workers"
print("changing the item value: ",Officelist)
print("\t")

#list through loop

print("iterating through for loop")
for i in Officelist:
     print(i)

print("\t")
print("check the existence of items")

#check the existence of items

Officelist2="employees" in Officelist
print(Officelist2)

#length of the list

print("\t")
print("length of the list: ",len(Officelist))
  
#adding elements into the list

print("\t")
print("adding elements into the list by 'insert','append' method")
listt=["Gadgets","apps","android"]
listt.insert(1,"mobapps")
print(listt)

listt.append("tech")
print(listt)

#removing elements

print("\t")
print("removing the elements by 'remove',pop' methods")

listt.remove("tech")
print(listt)
listt.pop()
print(listt)
print("\t")
print("combining two lists by '+' ,'extend' methods")

#combine two list

lt1=[1,2,3]
lt2=["apple","bat","cat"]
lt1.extend(lt2)
print(lt1)
lt3=lt1+lt2
print(lt3)