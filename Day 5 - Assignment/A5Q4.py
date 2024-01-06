"""
4. Create two lists to store cities and locations by accepting values from user.
Display 1st city and 1st location
then 2nd city and 2nd location ....... (zip function)
"""

lst1 = []
lst2 = []
q = ''
while q != 'NO':
    x = input("Enter City : ")
    y = input("Enter Location : ")
    lst1.append(x)
    lst2.append(y)
    q = input("Do you want to enter more inputs : [Yes/No]").upper()

for x,y in zip(lst1,lst2):
    print(x,"--->",y) 