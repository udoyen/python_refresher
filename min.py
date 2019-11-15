nums = [2, -1, 3, 5, 8, 9, 11]
letters = ['b', 'c', 'd', 'e', 'f']
names = ['emeka', 'baa', 'bassey', 'bab', 'joshua', 'joel', 'lizy']
fam = [2, 5, 3, 20, 4, 12, 100]
fam2 = [-0.3, -0.2, -0.5, -0.95, -0.9, -0.1]

def m_min(n):
    s = n[0]
    for i in n:
        if i < s:
            s = i
    print(s)

def m_max(n):
    s = n[0]
    for i in n:
        if i > s:
            s = i
    print(s)


def my_min(ls):
    n = 0
    zero_status = False
    state = False
    if isinstance(ls, list):
        for i in ls:
            if i <= n and state is False:
                n = i
            if i > n:
                state = True
                n = i
        print(n)
    else:
        print("The passed in argument is not a list")


# m_max(names)
m_min(names)