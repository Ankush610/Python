
list1 = []

n = int(input("Enter the amount of value you want to add : "))

for i in range(n):
    x = list(input("Enter Value : "))
    list1.append(x)

list1.sort(key = lambda x: x[1])

print(list1)