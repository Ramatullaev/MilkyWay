list1 = []
x = int(input())
list1.append(x)
while x != 0:
    x = int(input())
    list1.append(x)
print(list1.index(max(list1)))
