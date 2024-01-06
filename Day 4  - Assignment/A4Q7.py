def sum1(x):
    if x> 1:
        return x+sum1(x-1)
    elif x ==1:
        return x

def main(n):
    print(n, sum1(n))

n = int(input("Write a Number "))

if n <= 0:
    print("Write a number greater than 0 : ")
else:
    main(n)
