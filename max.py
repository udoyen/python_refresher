fam = [2, 5, 3, 20, 4, 12, 100]
gin = ()

def mymax(ls):
    n = 0
    if isinstance(ls, list):
        for i in range(0, len(ls)):
            for i in ls:
                if i > n:
                    n = i
        print(n)
    else:
        print("The passed in argument is not a list")

mymax(fam)
