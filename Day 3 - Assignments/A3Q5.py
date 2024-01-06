
#Incomeplete for 

# input variables
s1 = 'Abcdef'
s2 = 'Xyzw'
s2 = s2[::-1]

s = ''
w = ''

# Loop condition
if len(s1) < len(s2):
    x = len(s1)
else:
    x = len(s2)

#while -i-1 == j-1:
for i in range(x):
    s = s1[i]+s2[i]
    w = w + s

s3 = s1 + s2

m = list(w)

for i in s3:
    if i not in m:
        w = w + i

print(w)


