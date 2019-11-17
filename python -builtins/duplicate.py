f = [1, 2, 1, 3, 2, 5]

def duplicates(n):
    new = []
    for i in n:
        d = n.pop(0)
        if d in n:
            new.append(d)
    print(new)

duplicates(f)