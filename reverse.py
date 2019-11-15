a = [1, 2, 3, 4]

def reverse(ls):
    newls = []
    j = 0
    for i in ls:
        newls.insert(j, i)
        ++j

    print(newls)

reverse(a)