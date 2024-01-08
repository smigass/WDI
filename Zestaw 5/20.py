# Zadanie 20. Zadanie jak powyzej. Funkcja powinna dostarczyc droge króla w postaci tablicy zawierajacej
from helpers import random_list, list_table

moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, - 1), (-1, - 1)]


board = random_list(8, 50)
list_table(board)
