f = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
g = ["python", "java", "Python", "Java"]

def lensort(n):
    for i in range(len(n)):
        for j in range(len(n)):
            f1 = n[j]
            f2 = n[j + 1 if j != (len(n) - 1) else j]
            if len(n[j]) > len(n[j + 1 if j != (len(n) - 1) else j]):
                n[j] = f2
                n[j + 1 if j != (len(n) - 1) else j] = f1
    print(n)

lensort(f)