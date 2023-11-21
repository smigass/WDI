def get_palindromes(tab):
    si = None
    fi = None
    longest_p = 0
    for i in range(len(tab)):
        if tab[i] % 2 == 1 and not si:
            si = i
        if tab[i] % 2 == 0:
            fi = i
            if si:
                result = is_palindrome(tab[si:fi])
                if result:
                    if fi - si > longest_p:
                        longest_p = fi - si

                si = None
    return longest_p

def is_palindrome(t):
    ip = True
    print(t, t[-1])
    for i in range(len(t) // 2):
        if t[i] != t[-i - 1]:
            ip = False
    return ip


print(get_palindromes([2, 7, 5, 7, 5, 7, 2, 3, 9, 8]))
