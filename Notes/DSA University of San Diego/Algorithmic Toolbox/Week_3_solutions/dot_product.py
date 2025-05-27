from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product

def max_dot_product_fast(first_sequence, second_sequence):
    first_sequence.sort()
    second_sequence.sort()
    total_value = 0
    n = len(first_sequence)

    for i in range(n):
        total_value += first_sequence[i] * second_sequence[i]

    return total_value


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product_fast(prices, clicks))
    
