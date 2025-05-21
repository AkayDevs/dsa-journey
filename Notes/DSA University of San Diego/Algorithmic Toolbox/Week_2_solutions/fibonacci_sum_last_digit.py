def get_pisano_period(m):
    
    previous = 0
    current = 1
    for i in range(m*m):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i + 1

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_optimised(n):
    if n <= 1:
        return n
    
    rem = n % 60
    previous, current = 0, 1
    sum = 0
    for i in range(1, rem + 1):
        sum = ( sum + current ) % 10
        previous, current = current, previous + current
    
    return sum




if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_optimised(n))
