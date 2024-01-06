
a = 'this is fun'
b = ['a','e','i','o','u',' ']
k = []

for i in a:
    if i.lower() not in b:
        k.append(i+"o"+i)
    else:
        k.append(i)

print(''.join(k))
        
    
