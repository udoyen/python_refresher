from .sort_on_length import lensort

n = [1, 2, 3, 5, 6, 4, 10, 11, 12, 13, 14]
s = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']

def sort_by_size(n):
    state = False
    for i in n:
        if isinstance(i, str):
            state = True
    if state:
        lensort(n)
    else:
        for i in range(len(n)):
            for j in range(len(n)):
                pos1 = n[j]
                pos2 = n[j + 1 if j != (len(n) - 1) else j]
                if n[j] > n[j + 1 if j != (len(n) - 1) else j]:
                    n[j] = pos2
                    n[j + 1 if j != (len(n) - 1) else j] = pos1
    print(n)

if __name__ == '__name__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sort_by_size(n)