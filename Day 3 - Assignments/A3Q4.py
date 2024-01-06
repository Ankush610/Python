str1 = 'PytHONStudy'
low = ''
upp = ''
for i in str1:
    if i.isupper() == True:
        upp = upp + i
    else:
        low = low + i

print(low+upp)
        
