nums = [2, -1, 3, 5, 8, 9, 11, -2.3]
letters = ['b', 'c', 'd', 'e', 'f']
names = ['emeka', 'baa', 'bassey', 'bab', 'joshua', 'joel', 'lizy', 'zo', 'za']
fam = [2, 5, 3, 20, 4, 12, 100]
fam2 = [-0.3, -0.2, -0.5, -0.95, -0.9, -0.1]

def m_min(n):
    s = n[0]
    for i in n:
        if i < s:
            s = i
    print('Min Value: {}'.format(s))

def m_max(n):
    s = n[0]
    for i in n:
        if i > s:
            s = i
    print('Max Value: {}'.format(s))

m_max(fam2)
m_min(fam2)