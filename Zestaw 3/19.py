def check(t):
    for current_length in range(len(t), 0, -1):
        i = 0
        while i + current_length <= len(t):
            print(t[i:i+current_length])
            i += 1


check([1,2,3,4])

def 