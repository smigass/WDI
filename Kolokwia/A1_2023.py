T_org = [
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 2, 3, 7, 8, 9, 6],
    [3, 6, 9, 8, 4, 5, 7, 2, 1],
    [2, 8, 7, 1, 6, 9, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 3, 6, 8],
    [4, 3, 8, 5, 2, 6, 9, 1, 7],
    [7, 9, 6, 3, 1, 8, 4, 5, 2],
]

T_zad = [
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 3, 6, 8, 8, 9, 6],
    [3, 6, 9, 9, 1, 7, 7, 2, 1],
    [2, 8, 7, 4, 5, 2, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 2, 3, 7],
    [4, 3, 8, 5, 2, 6, 8, 4, 5],
    [7, 9, 6, 3, 1, 8, 1, 6, 9],
]

T = [
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 2, 3, 7, 3, 6, 8],
    [3, 6, 9, 8, 4, 5, 9, 1, 7],
    [2, 8, 7, 1, 6, 9, 4, 5, 2],
    [5, 2, 1, 9, 7, 4, 8, 9, 6],
    [4, 3, 8, 5, 2, 6, 7, 2, 1],
    [7, 9, 6, 3, 1, 8, 5, 3, 4],
]


def sudoku(T):
    s = suma(T)
    pom = [False, False, False]
    wrong_cols = [0, 0]
    wrong_rows = [0, 0]
    for i in range(9):
        row_sum = 0
        for j in range(9):
            row_sum += T[i][j]
        if row_sum != s:
            pom[i // 3] = True
    k = 0
    for v in range(3):
        if pom[v]:
            wrong_rows[k] = v
            k += 1
    pom = [False, False, False]
    for i in range(9):
        row_col = 0
        for j in range(9):
            row_col += T[j][i]
        if row_col != s:
            print(i)
            pom[i // 3] = True
    k = 0
    for v in range(3):
        if pom[v]:
            wrong_cols[k] = v
            k += 1
    print(wrong_rows, wrong_cols)


def suma(T):
    s = 0
    for i in range(3):
        for j in range(3):
            s += T[i][j]
    return s


print(sudoku(T_zad))
