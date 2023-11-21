def podzielniki_suma(number):
    tab = []
    for i in range(1,int(number**0.5) + 1):
        if number%i == 0: tab.append(i)
    for j in range(len(tab)-1,-1, -1):
        if number / tab[j] != tab[j] and number // tab[j] != number:
            tab.append(number//tab[j])
    return sum(tab)

def is_perfect(number):
    print(number)
    if number == podzielniki_suma(number): return True
    else: return False

perfect_numbers = []
for i in range(1,1000000):
    if is_perfect(i): perfect_numbers.append(i)

print(perfect_numbers)