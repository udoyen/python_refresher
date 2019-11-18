f = [1, 2, 1, 3, 2, 5]
s = ["python", "java", "Python", "Java", "java", "google", "Python", "Google", "gOOGLE", "google", "JAVA", "JavA"]


def unique(n, key=lambda s: s.lower()):
    new = []
    if isinstance(n, list):
        n = list(map(key, n))
    for a in n:
        d = n.pop(0)
        new.append(d)
        for j in n:
            if j == d:
                n.remove(j)
    print(new)


unique(s)