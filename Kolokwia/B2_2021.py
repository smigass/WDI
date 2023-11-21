import math


def roatations(n):
    l = int(math.log10(n)) + 1
    tab = [0 for i in range(l)]
    temp = n
    tab[0] = n
    for i in range(1, l):
        new_number = temp // 10 ** (l - 1)
        for j in range(1, l):
            last_digit = temp % 10
            new_number += last_digit * 10 ** j
            temp //= 10
        temp = new_number
        tab[i] = temp
    return tab




def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def iloczyn_w_systemie(n,sys):
    i = 0
    q = 1
    while n > 0:
        if n % sys < 10:
            q *= n % sys
        n //= sys
    return is_prime(q)



def sprawdz(n):
    rotations = roatations(n)
    for i in range(2, 16):
        for k in range(len(rotations)):
            if iloczyn_w_systemie(k, i):
                return i
    return 0




print(sprawdz(10799714))
