def fac(x):
    if x == 0:
        return 1
    else:
        return x*fac(x-1)
def main():
    for i in range(1,21):
        print(f"{i} = {fac(i)})")
main()





