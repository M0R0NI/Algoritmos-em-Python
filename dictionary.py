mydict = {"name": "Igor Moroni", "age": 23, "city": "São Paulo", "sonho": "Mercedes Benz"}
mydict["email"] = "igorjmv2017@hotmail.com"
print(mydict)

mydict2 = dict(name="Igor Moroni", age=23, city="São Paulo", sonho="Mercedes Benz")
del mydict2["city"]
print(f"{mydict2}\n")

for value in mydict2.values():
    print(value)
for key, value in mydict2.items():
    print(key, value)

valor = mydict["name"]
value = mydict["sonho"]
print(f"\n{valor}")
print(value)