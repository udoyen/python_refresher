s = ['a', 'b', 'c', 'd', 'e', 'f']

def cummulative_sum(n):
    for i in range(len(n) - 1):
        n[i + 1] += n[i]
    print(n)    

cummulative_sum(s)