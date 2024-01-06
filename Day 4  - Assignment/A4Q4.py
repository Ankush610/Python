'''
4. A pangram is a sentence that contains all the letters of the English alphabet at least once, for
example: The quick brown fox, jumps over the lazy dog!!!!.
Your task here is to write a function to check a sentence to see if it is a pangram or not.

'''

a = 'The quick brown fox, jumps over the lazy dog!!!!'
k = []
for i in a:
    k.append(i.lower())
c = 0
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in a:
    if i in k:
        c = c + 1
    else:
        pass

if c == 26:
    print("Given Sentence is a Panagram")
else:
    print("Given Sentence is not a Panagram")
    
    
    

