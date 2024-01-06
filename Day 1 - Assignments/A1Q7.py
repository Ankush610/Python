n = int(input("Enter Eletricity Bills : "))
a = 0
if n<=100:
    print("No Charge")
elif n>100:
    if n<200:
        n = n - 100
        a = a + n*5
    elif n>200:
        a = a + 100*5
        n = n-200
        a = a + n*10
print(a)

     
