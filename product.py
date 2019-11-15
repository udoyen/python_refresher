items = [1, 2, 3, 5]

def product(a):
    c = 1
    for i in a:
        c *= i

    print(c)

def factorial(f):
    # create a list
    ls = [x for x in range(1, (f + 1))]
    product(ls)

# product(items)
factorial(4)