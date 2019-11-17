list = [3, 3, 2, 1, 0, 9, 8]
name = ['george', 'udosen']

def d_sum(some_list):
    r = None    
    for j in some_list:
        if isinstance(j, str):
            r = ""
        else:
            r = 0
    for i in some_list:
        r += i
    print(r)

d_sum(name)
