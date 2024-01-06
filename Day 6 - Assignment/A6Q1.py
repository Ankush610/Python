
#----A6Q1

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red","Yellow","orange"]

sampleSet.update(sampleList)
print(sampleSet)

#----A6Q2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

#----A6Q3

set1 = {10, 20, 30, 40, 50,25}
set2 = {30, 40, 50, 60, 70,100}

set3 = set1.symmetric_difference(set2)

print(set3)

#----A6Q4

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))
print(set1.intersection(set2))

print(set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print(set1)

print(set1.difference(set2))
set1 = {10, 20, 30, 40, 50}
set1.difference_update(set2)
print(set1)

#----A6Q5

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

avg = sum(set2)/len(set2)

set3 = {i for i in set2 if i > avg}
set1.update(set3)
print(set1)

#----A6Q6

a = set()
x = int(input("How many Values you want to Enter : "))
while True:
    
    n = input("Enter value : ")
    a.add(n)
    if len(a) == x:
        break

b = {i for i in a if len(i) > len(a)}
print(b)


