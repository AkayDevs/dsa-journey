def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_optimised(numbers):
    max_1, max_2 = max(numbers[0], numbers[1]), min(numbers[0], numbers[1])
    n = len(numbers)
    for i in range(2, n):
        if numbers[i] > max_1:
            max_2 = max_1
            max_1 = numbers[i]
        elif numbers[i] <= max_1 and numbers[i] > max_2:
            max_2 = numbers[i]
    
    return max_1 * max_2


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_optimised(input_numbers))
