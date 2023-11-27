# Zadanie 16. Wyrazy budowane sa z liter a..z. Dwa wyrazy ”waza” tyle samo jezeli: maja te sama liczbe samogłosek
# oraz sumy kodów ascii liter z których sa zbudowane sa identyczne, na przykład ula -> 117, 108, 97, 1
# oraz 00exe00 ! 101, 120, 101. Prosze napisac funkcje wyraz(s1,s2), która sprawdza czy jest mozliwe zbudowanie
# wyrazu z podzbioru liter zawartych w s2 wazacego tyle co wyraz s1. Dodatkowo funkcja powinna wypisac
# znaleziony wyraz.

def samogloski(w):
    cnt = 0
    for l in w:
        if l == "a" or l == "i" or l == "o" or l == "e" or l == "u" or l == "y":
            cnt += 1
    return cnt


def check(s1, s2):
    if len(s1) == len(s2):
        if len(s1) == 0:
            return False, s1, s2
        if sum([ord(a) for a in s1]) == sum(ord(b) for b in s2):
            return True, s1, s2
    return False, s1, s2


def rek(s1, s2, w1="", w2="", i=(0, 0)):
    res, r1, r2 = check(w1, w2)
    if res:
        return res, r1, r2
    if i[0] == len(s1) and i[1] == len(s2):
        return False
    if i[0] == len(s1):
        i = (i[0] - 1, i[1])
    if i[1] == len(s2):
        i = (i[0], i[1] - 1)
    return (rek(s1, s2, w1, w2, (i[0] + 1, i[1] + 1)) or
            rek(s1, s2, w1 + s1[i[0]], w2, (i[0] + 1, i[1] + 1)) or
            rek(s1, s2, w1, w2 + s2[i[1]], (i[0] + 1, i[1] + 1)) or
            rek(s1, s2, w1 + s1[i[0]], w2 + s2[i[1]], (i[0] + 1, i[1] + 1)))


def wyraz(s1, s2):
    return rek(s1, s2)


print(wyraz("ula", "exe"))
