

list1 = [[]]

n = int(input("Enter the amount of value you want to add : "))

for i in range(n):
    x = list(map(int,input("Enter Digit : ").split()))
    y = x[-1]%10
    list1.insert(y,x)

print(list1)

