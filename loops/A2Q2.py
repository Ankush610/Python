
#Half Pyradmid

n = int(input("Enter The Number : "))

for i in range(n+1):
    print("*"*i)

print()

#Diamond

k = n//2
x = 1
for i in range(n+1):
    print(k*" "+"* "*x)
    if i < n//2:
        k = k - 1
        x = x + 1
    else:
        k = k + 1
        x = x - 1

print()

# One sided pyramid of 0's and 1's

num = 0
p = n//2
while num < n//2:
    p = p - 1
    for j in range(p):
        print('1',end=' ')
        print('0',end=' ')
    print(1)
    num += 1

print()

# pyramid of 0's and 1's

num = 0
p = n
while num < n:
    print(' '*num,end='')
    p = p - 1
    for j in range(p):
        print('1',end=' ')
        print('0',end=' ')
    print(1)
    num += 1

print()

k = 1
while k <= n+1:
    for i in range(1,k):
        print(i,end=' ')
    print()
    k = k + 1

