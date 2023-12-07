from helpers import list_table
from sudoku_generator import Sudoku


def sudokuCheck(grid):
    # edge cases
    if not grid:
        return False

    # rows by rows checking
    hset = set()
    for i in range(9):
        for j in range(9):
            if grid[i][j] in hset:
                return False
            else:
                hset.add(grid[i][j])
        hset = set()

    # cols by cols checking
    hset = set()
    for i in range(9):
        for j in range(9):
            if grid[j][i] in hset:
                return False
            else:
                hset.add(grid[j][i])
        hset = set()

    # 3 by 3 check
    subs = [range(0, 3), range(3, 6), range(6, 9)]
    subgrids = []
    for x in subs:
        for y in subs:
            subgrids.append([x, y])
    for (row_range, column_range) in subgrids:
        hset = set()
        for i in row_range:
            for j in column_range:
                if grid[i][j] in hset:
                    return False
                else:
                    hset.add(grid[i][j])

    return True


def sudoku_solver(tab, empty_tab, index=0):
    if index == len(empty_tab):
        list_table(tab)
        print(sudokuCheck(tab))
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
