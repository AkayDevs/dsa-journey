import random


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
    for i in range(2, len(numbers)):
        if numbers[i] > max_1:
            max_2 = max_1
            max_1 = numbers[i]
        elif numbers[i] <= max_1 and numbers[i] > max_2:
            max_2 = numbers[i]
    
    return max_1 * max_2



def stres_test() :

    while True:
        n = random.randint(2, 1000)
        nums = [random.randint(1, 100000) for i in range(n)]
        ans_slow = max_pairwise_product(nums)
        ans_optim = max_pairwise_optimised(nums)

        if ans_optim != ans_slow:
            print(f"Wrong Answer: slow -> {ans_slow}  fast -> {ans_optim}")
            print(f"n : {n}")
            print(nums)
            break

        else: 
            print("OK")


if __name__ == '__main__':
    stres_test()