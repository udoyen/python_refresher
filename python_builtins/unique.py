f = [1, 2, 1, 3, 2, 5, 6, 5, 5, 4, 4, 4, 4, 10, 10, 11, 12, 13, 14, 6, 5]
s = ["python", "java", "Python", "Java", "java", "google", "Python", "Google", "gOOGLE", "google", "JAVA", "JavA"]


def unique(n, key=lambda s: s.lower()):
    new = []
    state = False
    for k in n:
        if isinstance(k, str):
            n = list(map(key, n))
            state = True
    if state:
        for a in n:
            d = n.pop(0)
            new.append(d)
            for j in n:
                if j == d:
                    n.remove(j)
    else:
        for a in range(len(n)):
            if len(n) == 0:
                break
            d = n.pop(0)
            if d not in new:
                new.append(d)
            for j in n:
                if j == d:
                    n.remove(j)
    print(new)


unique(f)