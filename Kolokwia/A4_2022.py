from listowanie import listuj

# TODO - Do poprawy
N = 9
# T = [[0 if random.random() < 0.85 else 1 for _ in range(N)] for _ in range(N)]
T = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
listuj(T)


def place(t):
    n, min_dist = len(t), len(t)
    middle = (n / 2, n / 2)
    max_new = 0
    best = None
    possible_checks = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for row in range(n):
        for col in range(n):
            if t[row][col] == 1: continue
            dist = max(abs(middle[0] - row), abs(middle[1] - col))
            new = 0
            for p in possible_checks:
                virtual_move = row + p[0], col + p[1]
                if 0 <= virtual_move[0] < n and 0 <= virtual_move[1] < n:
                    if t[virtual_move[0]][virtual_move[1]] == 0:
                        new += 1
            if new > max_new:
                max_new = new
                best = row, col
            elif new == max_new and min_dist > dist:
                min_dist = dist
                best = row, col
    return best


print(place(T))
