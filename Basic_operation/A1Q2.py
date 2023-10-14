n = int(input("Enter Amount : "))
a = [2000,500,100,50,10,5,2,1] #Type of Notes
b = [0,0,0,0,0,0,0,0] #Count of Notes

while n > 0:
    if n >= a[0]:
        n = n - a[0]
        b[0] = b[0] + 1
    elif n >= a[1]:
        n = n - a[1]
        b[1] = b[1] + 1
    elif n >= a[2]:
        n = n - a[2]
        b[2] = b[2] + 1
    elif n >= a[3]:
        n = n - a[3]
        b[3] = b[3] + 1
    elif n >= a[4]:
        n = n - a[4]
        b[4] = b[4] + 1
    elif n >= a[5]:
        n = n - a[5]
        b[5] = b[5] + 1
    elif n >= a[6]:
        n = n - a[6]
        b[6] = b[6] + 1 

for i in range(len(b)):
    if b[i] != 0:
        print(a[i],b[i])


