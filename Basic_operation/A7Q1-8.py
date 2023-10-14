
#-------------- A7Q1
print()

keys = ['Ten', 'Twenty', 'Thirty', 'Forty']
values = [10, 20, 30]
dic1 = {}

for i in range(len(keys)):
    if i < len(values):
        dic1[keys[i]] = values[i]
    else:
        dic1[keys[i]] = None
print(dic1)

print()

#--------------- A7Q2

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1,**dict2}

print(dict3)

print()

#--------------- A7Q3


sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(sampleDict['class']['student']['marks']['history'])

print()

#--------------- A7Q4

sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
#keysToRemove = ["name", "salary"]
sampleDict

print()
#--------------- A7Q5

sampleDict = {'a': 100, 'b': 200, 'c': 300,'d':200}

for k,v in sampleDict.items():
    if v == 200:
        print(f"{k} ---> {v}")

print()
#--------------- A7Q6

sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
val = sampleDict['city']
sampleDict.pop('city')
sampleDict['location'] = val
print(sampleDict)

print()
#--------------- A7Q7

sampleDict = {'Physics': 82,'Math': 65,'history': 75}

temp = 0
for v in sampleDict.values():
    if v > temp:
        temp = v
        
for k,v in sampleDict.items():
    if v == temp:
        print(k)

print()
# ------------------- A7Q8

sampleDict = {'emp1': {'name': 'Jhon', 'salary': 7500},'emp2': {'name': 'Emma', 'salary': 8000},'emp3': {'name': 'Brad', 'salary': 6500}}

for k,v in sampleDict.items():
    key = input("Enter the name : ")
    if v['name'] == key:
        value = int(input("Enter the new salary : "))
        if v['salary'] < value:
            v['salary'] = value
            break
        else:
            print("New Salary Should be Larger than Previous")
            break
    else:
        print("Name not found")
        break

print(sampleDict)