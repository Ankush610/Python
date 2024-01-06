x = int(input("Enter the Number : "))
n = int(input("Enter the size of series : "))
s = 1 + x
print(s)

for i in range(2,n):
    k = 1
    for j in range(1,i+1):
        k = k*j    
    z = x**i
    s = s + z/k
    print(f"for {x}^{i}/{k} result {s}")

print(round(s,2))

