f = [1, 2, 1, 3, 2, 5]

def unique(n):
    new = []
    for i in range(len(n)):
        d = n.pop(0)        
        if d in n:
            new.append(d)
            n.remove(d)
        else:
            new.append(d)
        if len(n) == 0:
            break
    print(new)


unique(f)