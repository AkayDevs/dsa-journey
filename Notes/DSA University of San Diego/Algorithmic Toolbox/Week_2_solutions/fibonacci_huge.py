def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def calculate_pisano(m):

    previous = 0
    current = 1

    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def fibonacci_huge_optimised(n, m):
    pisano_p = calculate_pisano(m)
    rem = n % pisano_p

    if rem <= 1:
        return rem

    previous = 0
    current = 1
    for i in range(2, rem + 1):
        previous, current = current, (previous + current)

    return current % m



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_optimised(n, m))
    # print(f"Pisano Period of 3 : {calculate_pisano(1000)}")
