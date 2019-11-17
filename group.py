f = [1, 2, 3, 4, 5, 6, 7, 8, 9]
g = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def group(ls, n):
    mother = []
    div = int(len(ls) / n)
    rem = len(ls) % n
    if isinstance(ls, list) and isinstance(n, int):
        if len(ls) >= n:
            for i in range(div):
                child = []
                for j in range(n):
                    for l in ls:
                        child.append(ls.pop(0))
                        break
                        
                mother.append(child)
            if rem > 0:
                child = []
                for k in range(rem):
                    child.append(ls.pop())
                mother.append(child)
        else:
            print('List length should be grester than the divisor')
        print(mother)
    else:
        print('Wrong arguments! ls = List and n = int required')

group(f, 2)