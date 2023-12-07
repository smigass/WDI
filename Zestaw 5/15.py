# Zadanie 15. Problem 8 Hetmanów (tresc oczywista)
# Chodzi o to, że trzeba ustawić 8 hetmanów na szachownicy 8 x 8 tak, aby żadne dwa hetmany się nie szachowały

from helpers import list_table


def reformat(uc):
    t = [["•" if uc[j] != i else "H" for i in range(8)] for j in range(8)]
    return t


counter = 0


def hetman(used_cols, dgl1, dgl2, row=0):
    global counter
    # warunek zakończenia (może być if row == 8)
    if row == 8:
        counter += 1
        print(f"rozwiazanie {counter}:", end="")
        list_table(reformat(used_cols))
    else:
        for col in range(8):
            if col not in used_cols and not dgl1[row + col] and not dgl2[col - row + 7]:
                used_cols[row] = col
                # dgl1 - przekatne /
                # dgl2 - przekatne \
                dgl1[row + col] = True
                dgl2[col - row + 7] = True
                hetman(used_cols, dgl1, dgl2, row + 1)
                dgl1[row + col] = False
                dgl2[col - row + 7] = False
                used_cols[row] = -1


hetman([-1 for _ in range(8)], [False for _ in range(15)], [False for _ in range(15)])
