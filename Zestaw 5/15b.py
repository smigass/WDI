# Zadanie ciekawostkowe (15 dla dowolnego n)

from helpers import list_table


def reformat(uc):
    luc = len(uc)
    t = [["⚪" if uc[j] != i else "🔴"for i in range(luc)] for j in range(luc)]
    return t


counter = 0


def hetman(used_cols, dgl1, dgl2, row=0):
    global counter
    n = len(used_cols)
    # warunek zakończenia (może być if row == 8)
    if row == n:
        counter += 1
        print(f"rozwiazanie {counter}:", end="")
        list_table(reformat(used_cols))
    else:
        for col in range(n):
            if col not in used_cols and not dgl1[row + col] and not dgl2[col - row + n -1]:
                used_cols[row] = col
                # dgl1 - przekatne /
                # dgl2 - przekatne \
                dgl1[row + col] = True
                dgl2[col - row + n - 1] = True
                hetman(used_cols, dgl1, dgl2, row + 1)
                dgl1[row + col] = False
                dgl2[col - row + n - 1] = False
                used_cols[row] = -1


N = 8
hetman([-1 for _ in range(N)], [False for _ in range(2 * N - 1)], [False for _ in range(2 * N - 1)])
