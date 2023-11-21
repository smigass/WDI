# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.


def decimal_to_binary(n):
    binary = 0
    power = 0
    while True:
        binary += n % 2 * 10 ** power
        power += 1
        if n == 1:
            break
        n = n // 2
    return binary


number = int(input("Podaj liczbę naturalną: "))

def is_palindrome(n):
    l = len(str(n))
    p = n
    for i in range(0, l // 2):
        left = n // 10 ** (len(str(n)) - 1)
        right = n % 10
        n -= n % 10
        n -= n // 10 ** (len(str(n)) - 1) * 10 ** (len(str(n)) - 1)
        n //= 10
        if left != right:
            return f"Liczba {p} nie jest palindromem"
    return f"Liczba {p} jest palindromem"


print(is_palindrome(number))
print(is_palindrome(decimal_to_binary(number)))