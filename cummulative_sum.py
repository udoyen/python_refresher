s = ['a', 'b', 'c', 'd', 'e', 'f']
t = [1, 2, 3, 4]
u = [4, 3, 2, 1]

def cummulative_sum(n):
    for i in range(len(n) - 1):
        n[i + 1] += n[i]
    print(n)

def cummulative_prod(n):
    for i in range(len(n) - 1):
        n[i + 1] *= n[i]
    print(n)

# cummulative_sum(t)
cummulative_prod(s)