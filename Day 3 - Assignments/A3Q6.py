str1 = "Welcome to USA, usa awesome,isn't it?"
strup = str1.upper()
print(strup)
a = "USA"
pos = strup.rfind(a)

while pos != -1:
    print(pos)
    pos = strup.rfind(a,0,pos)
    

print(strup.count(a))
