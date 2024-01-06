
s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

n = len(s1)

if n%2 == 0:
    x = int(n/2)
    y = int(n/2)
    print(s1[:x]+s2+s1[y:])
else:
    x = input("You have entered odd charactered,\nDo you want to exclde Center Character to make proper Center , press [Y/N] : ").upper()
    if x == 'Y':
        print("Exculding center character from odd charactered string : ")
        x = int(n/2-0.5)
        y = int(n/2+0.5)
        print(s1[:x]+s2+s1[y:])
    elif x == 'N':
        print("Not Exculding center character from odd charactered string : ")
        x = int(n/2)
        y = int(n/2)
        print(s1[:x]+s2+s1[y:])
    else:
        print("Give Proper Input")
