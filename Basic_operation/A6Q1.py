#reverse Function
lst = [100,200,300,400,500]
lst.reverse()
print(lst)

#zip function
a = ['M','na','i','raj']
b = ['Y','me','s','esh']
c = [a+b for a,b in zip(a,b)]
print(c) 

#--or--
c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)   

#list comprihension
a = [1,2,3,4,5,6,7]
b =  [x**2 for x in a]
c = list(map(lambda x : x**2 ,a))
print(b)
print(c)

#
a = ['Hello','Welcome']
b = ['Studnet','Sir']

c = [a[i]+b[j] for i in range(len(a)) for j in range(len(b))]
print(c)

a = [10,20,30,40]
b = [100,200,300,400]
b.reverse()
c = [[a[i],b[i]] for i in range(len(a))] #Using Range
d = [[x,y] for x,y in zip(a,b)] #Using zip
print(c)
print(d)

a = ['Ashish','','Atharva','Amit','','Revti']
b = [i for i in a if i != '']
print(b)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2][2].insert(2,1)
print(list1)

