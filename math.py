from random import choice, sample
a= {i for i in range(1,47)}
a.add("D0123456")
while True:
    x=a.pop()
    if x=="D123456":
        a.add(x)
    else:
        break
print(x)
for i in range(6):
    print((a.pop(), "Warning"))
b= {i for i in range(1,47)}
print(b.difference(a))
a.remove("D123456")
print(a)
print(len(a))

