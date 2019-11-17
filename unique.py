f = [1, 2, 1, 3, 2, 5]
s = ["python", "java", "Python", "Java"]

def unique(n, key=lambda s: s.lower()):
    new = []
    for a in n:
        if isinstance(a, str):
            n = list(map(key, n))
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


unique(s)