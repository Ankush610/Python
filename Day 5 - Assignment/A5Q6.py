'''
# This part Remaining 
print("6. convert set into frozenset")

'''

a = set()
b = set()

def delset(x): # 1.
    if x == 'a':
        x = input("Enter the value to be deleted : ")
        a.remove(x)
        
    else:
        x = input("Enter the value to be deleted : ")
        b.remove(x)
        

def addele(): # 2.
    print("Set Created Sucessfully...")
    y = int(input("How many Enteries you want in second set : "))
    for i in range(y):
        x = input("Enter Input : ")
        a.add(x)

def union(): # 4.
    x = a.union(b)
    print(x)

def createset():
    print("Second Set Created Sucessfully...")
    y = int(input("How many Enteries you want in second set : "))
    for i in range(y):
        x = input("Enter Input : ")
        b.add(x)

def intersect(): # 5.
    x = a.intersection(b)
    print(x)

def difference(): #6.
    x = a.difference(b)
    print(x)

def frozenset(): # 7.
    
    pass

while True: 
    case = int(input("""
                    1. delete element
                    2. add a elemet
                    3. create one more set
                    4. union of 2 sets
                    5. intersection of 2 sets
                    6. difference of 2 sets
                    7. convert set into frozenset
                    8. Print set
                    9. Exit
                    Enter Choice:"""))



    if case == 1:
        x = input("""Enter from which set you want to delete element : 
        1. Set a
        2. Set b
        choice [a/b]: """)
        if x == 'a':
            delset('a')
        elif x == 'b':
            delset('b')
        
    if case == 2:
        addele()

    if case == 3:
        createset()

    if case == 4:
        union()

    if case == 5:
        intersect()

    if case == 6:
        difference()

    if case == 7:
        frozenset()

    if case == 8:
        x = input("""Enter which set you want to print : 
        1. Set a
        2. Set b
        3. Set a and b 
        choice [a / b / ab]: """)
        if x == 'a':
            print(a)
        elif x == 'b':
            print(b)
        elif x == 'ab':
            print(a,b)

    if case == 9:
        print("Exiting......")
        break

            



