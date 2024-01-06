
lst = []

def additemf():
    x = input("Enter a Value to Add : ")
    lst.append(x)
    print("Item Added Sucessfully...")

def additeml():
    x = input("Enter a Value to Add : ")
    y = int(input("Enter a position : "))
    lst.insert(y,x)
    print("Item Added Sucessfully...")

def deliteml():
    lst.pop()
    print("Item Deleted Sucessfully...")

def delitem():
    x = input("Enter the Value to Delete : ")
    lst.remove(x)
    print("Item Deleted Sucessfully...")

def delitemin():
    x = input("Enter the index to delte item from : ")
    del(lst[x])

def sortf():
    lst.sort()

def sortr():
    lst.sort(reverse=True)


while True:
    case = input("""
1. Accept Data
2. Delete data by value
3. delete data by position
4. sort
5. reverse
6. Display in sorted order without changing original list
7. Display in reverse order without changing original list 
8. display data
9. Exit...\nchoose: 
""")
    if case == '1':
        x = input("a) add at last position\nb) add at given position \nchoose: ")
        if x == 'a':
            additemf()
           
        elif x == 'b':
            additeml()
            
    elif case == '2':
        delitem()

    elif case == '3':
        x = input("a) delete last element\nb) delete from particular position \nchoose: ")
        if x == 'a':
            deliteml()
        elif x == 'b':
            delitemin()
            
    elif case == '4':
        x = input("a) ascending\nb) descending \nchoose: ")
        if x == 'a':
            sortf()
        elif x == 'b':
            sortr()

    elif case == '5':
        lst.reverse()

    elif case == '6':
        x = sorted(lst)
        print(x)

    elif case == '7':
        x = sorted(lst,reverse=True)
        print(x)

    elif case == '8':
        x = input("a) normal\nb) numbered \nchoose: ")
        if x == 'a':
            print(lst)
            
        elif x == 'b':
            for x,y in enumerate(lst):
                print([[x,y]])
        
    elif case == '9':
        print("Thank you for visiting ... ")
        break

