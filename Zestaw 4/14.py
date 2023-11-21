def to_binary(n, t):
    if n > 0:
        return to_binary(n // 2, [n % 2]+t)
    return t

print(to_binary(53, []))