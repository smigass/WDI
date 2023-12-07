from helpers import list_table
from sudoku_generator import Sudoku


def sudoku_solver(tab, empty_tab, index=0):
    if index == len(empty_tab):
        list_table(tab)
    else:
        row = empty_tab[index][0]
        col = empty_tab[index][1]
        possibilities = get_possible_numbers(tab, empty_tab[index])
        for num in possibilities:
            tab[row][col] = int(num)
            sudoku_solver(tab, empty_tab, index + 1)
            tab[row][col] = 0


def square_missing(point, tab):
    s = '123456789'
    row = point[0] // 3
    col = point[1] // 3
    for i in range(3 * row, 3 * row + 3):
        for j in range(3 * col, 3 * col + 3):
            num = tab[i][j]
            s = s.replace(str(num), "")
    return s


def get_possible_numbers(tab, point):
    s = square_missing(point, tab)
    return row_col_missing(point, tab, s)


def row_col_missing(point, tab, s):
    for i in range(9):
        num = tab[point[0]][i]
        s = s.replace(str(num), "")
    for j in range(9):
        num = tab[j][point[1]]
        s = s.replace(str(num), "")
    return s


sudoku = Sudoku(9, 40)
sudoku.fillValues()
list_table(sudoku.mat)
empty = sudoku.get_empty_points()
sudoku_solver(sudoku.mat, empty)
