n = int(input("Enter The Year : "))

if n > 0:
    if n%100 == 0:
        if n%400 == 0:
            print(f"{n} is a leap Year")
        else:
            print(f"{n} is Not a leap Year")
    elif n%4==0 and n%100 != 0:
        print(f"{n} is a leap Year")
    else:
        print(f"{n} is Not a leap Year")
else:
    print("A Year Cannot be Negative")
