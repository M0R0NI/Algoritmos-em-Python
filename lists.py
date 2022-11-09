# Listas ordenadas, mutáveis e que permitem elementos duplicados.

mylist = ["Mercedes-Benz", "BMW", "Audi", "Lamborghini", "Ferrari", "Porsche"]
print(mylist)

item = mylist[4]
print(item)

for i in mylist:
    print(i)

if "Lamborghini" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.append("Jaguar")
print(mylist)

mylist.insert(5, "Maserati")
print(mylist)

item = mylist.remove("Audi")
print(mylist)

item = mylist.reverse()
print(mylist)

item = mylist.sort()
print(mylist)

newlist = [7] * 3
print(newlist)

newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = newlist[2:9]
print(x)

newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = [i*i for i in newlist]
print(x)

item = mylist.clear()
print(mylist)
