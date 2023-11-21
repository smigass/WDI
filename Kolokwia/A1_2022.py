# Dana jest tablica T zawierająca liczby naturalne. W tablicy na kolejnych pozycjach ukryto pewien ciąg liczb
# o długości co najmniej 3 elementów. Aby ułatwić odnalezienie tego ciągu, zaraz za nim umieszczono ten sam
# ciąg ale każdy z jego elementów pomnożono przez pewną liczbę. Proszę napisać funkcję sequence(T)
# która odnajdzie ukryty ciąg. Funkcja powinna zwrócić indeksy pierwszego i ostatniego elementu ukrytego ciągu.


def sequence(T):
    length = 3
    n = len(T)
    found = False
    beg = 0
    while not found:
        current_max = 1
        k = T[length] / T[0]
        for i in range(1, n - length):
            if T[i + length] / T[i] == k:
                current_max += 1
            else:
                if current_max >= 3:
                    return beg, i - 1
                k = T[i + length] / T[i]
                current_max = 1
                beg = i
        length += 1
    return False

print(sequence( [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]))
