number = 202542342

def find(number):
    limit = 3
    while limit < 50000:
        for i in range(1,limit):
            j = limit - i
            if fib(i,j,number):
                return i,j
        limit += 1
    

def fib(a,b, n):
    tab = []
    while b <= n:
        tab.append(b)
        a,b = b, a+b
        if a == n:
            print(tab)
            return True
    return False



print(find(number))

