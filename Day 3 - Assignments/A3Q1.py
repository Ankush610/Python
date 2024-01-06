
a = input("Enter a String of odd length greater than 7 : ")
n = len(a)

print(type(n))
x = int(n/2-1.5)
y = int(n/2+1.5)

if n > 7 and n%2 != 0:
    print(a[x:y])
else:
    print('Give a proper Input')

