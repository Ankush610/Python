n = int(input("Enter max size of Digits in Seires : "))
s = 0
b = 9
c = 0
k = []
for i in range(n):
    c = c + b
    s = s + c
    b = b*10
    k.append(c)
    
print(f"The Seires is {k} and the sum is : {s}")
