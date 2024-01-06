'''

Define a procedure histogram() that takes a list of integers and prints a histogram to the
screen. For
example, histogram([4, 9, 7]) should print the following:
****
*********
*******

'''

def histogram(x):
    for i in range(len(x)):
        print("* "*x[i])

a = [4,7,9]
histogram(a)
