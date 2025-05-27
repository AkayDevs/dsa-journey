from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def largest_number_fast(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: int(x[0]), reverse=True)
    return int("".join(numbers))


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_fast(input_numbers))
