fam = [2, 5, 3, 20, 4, 12, 100]
fam2 = [-0.3, -0.2, -0.5, -0.95, -0.9, -0.1]
gin = ()

# @profile
def mymax(ls):
    n = 0
    zero_status = False
    state = False
    if isinstance(ls, list):
        for i in ls:
            if i <= n and state is False:
                n = i
            if i > n:
                state = True
                n = i
        print(n)
    else:
        print("The passed in argument is not a list")

if __name__ == "__main__":
    mymax(fam2)
