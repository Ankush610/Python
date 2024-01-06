
a = ["Go hang a salami I'm a lasagna hog.","Was it a rat I saw?","Step on no pets","Sit on apotato pan, Otis",
     "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamedunder it as a tired nude Maori",
     "Rise to vote sir","Dammit, I'm mad!"]


#b = a[1]
b = input("Enter your Senetence : ")
O = []
R = []
for i in b:
    if i not in [' ','~','`','!','@','#','$','%','^','&','*','(',')','_','+','}','{',':','"','?','>','<','|','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\',''',';','.',',','/',"'"]:
        O.append(i)

# Original sentence    
R = O.copy()
Org = ''.join(O).lower()
print(Org)

# reversed sentence
R.reverse()
Rev = ''.join(R).lower()
print(Org)

if Org == Rev:
    print("It is a palandrome !")
else:
    print("It is not a palandrome")




