n = 10000

def find_iteration(n):
    max_iterations = 0
    best_first = 0
    for i in range(2, n+1):
        steps = 1
        previous_element = next_in_sequence(i)
        while previous_element != 1:
            steps += 1
            previous_element = next_in_sequence(previous_element)
        if steps > max_iterations:
            max_iterations = steps
            best_first = i
    return (max_iterations, best_first)


def next_in_sequence(previous):
    return (previous % 2) * (3 * previous + 1) + (1 - previous % 2) * (previous / 2)


print(find_iteration(n))