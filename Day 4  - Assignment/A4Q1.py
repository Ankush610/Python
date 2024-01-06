
#n = int(input("Enter the no of Weeks : "))
m = int(input("Enter the no of months : "))
k = int(input("""
1.monday
2.Tuesday
3.Wednesday
4.Thursday
5.Friday
6.Saturday
7.sunday
Enter the day the month starts with : """))

g = k - 1
h = 0
a = []

b = ['Mo','Tu','We','Th','Fr','Sa','Su']

# to make list of Days
        
for j in range(1,m-21):
    a.append(' '+str(j))

for i in range(10,m+1):
    a.append(str(i))

print()


for i in b:
    print(i,end="  ")
print()

for i in range(7):
    if i < g:
        print('  ',end='  ')
        
h = 8 - k
for i in range(h):
    print(a[i],end='  ')
print('\n')

for i in range(h-1):
    a.pop(0)


for i in range(1,len(a)):
    if i%7 != 0 :
        print(a[i],end='  ')
    else:
        print(a[i]+'\n')








 
    
    
        
 

    
