a = int(input("Enter the Number : "))
b = s = count = 0
while a > 0:
    b = a%10
    a = a//10
    s = s + b
    count += 1

print(f"Sum is {s} and Count is {count}")
    
