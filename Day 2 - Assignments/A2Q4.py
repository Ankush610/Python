k = []
q = ''
a = 0
b = 1
while q != 'q':
    n = int(input("Enter the Number : "))
    q = input("Press [q] if You want to quit : ")
    k.append(n)

for i in range(len(k)):
    a = a + k[i]
    b = b * k[i]

avg = a/len(k)

print(f"The Average of Entered Numbers : {avg} \nThe Product of Entered numbers {b}")



    
