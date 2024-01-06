"""
5. Create a list and exchange the values as index and index as values.
lst=[12, 1, 3, 7, 8, 5, 8]
      0  1  2  3  4  5  6
"""

lst=[12, 1, 3, 7, 8, 5, 8]
lst2 = [-1 for i in range(len(lst))]
print(lst2)
for x,y in enumerate(lst):
    key = x
    val = y
    lst2.insert(val,key)

print(lst2)




