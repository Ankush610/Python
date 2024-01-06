s1 = 'America'
s2 = 'japan'

x = len(s1)
y = len(s2)

ans = s1[0]+s2[0]+s1[int(x//2)]+s2[int(y//2)]+s1[-1]+s2[-1]
print(ans)
