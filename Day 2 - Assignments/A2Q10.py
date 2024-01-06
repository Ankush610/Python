x = int(input("input the value of x : "))
n = int(input("input the number of terms : "))

s = 0
i = 0
c = 0
while c <= n:
    if i%2 != 0: 
        v = x**i
        if c%2 != 0:
            s = s + v
            print(f"{x}^{i} :",v)
        else:
            s = s - v
            print(f"{x}^{i} :",-v)
        
    i = i + 1
    if i%2 != 0:
        c = c + 1

print(f"The final sum is : {s}")
