a = int(input("Enter First Input : "))
b = int(input("Enter Second Input : "))
k = []

for i in range(1,a):
    if a%i == 0 and b%i == 0:
        k.append(i)
    else:
        continue

print(k[len(k)-1])
    
        
