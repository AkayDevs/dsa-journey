# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

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

def fibonacci_partial_sum_fast(from_, to):

    to_sum = fibonacci_sum_optimised(to)
    if from_ == 0:
        return to_sum
    
    from_sum = fibonacci_sum_optimised(from_)
    return (to_sum - from_sum) if to_sum >= from_sum else (10*to_sum - from_sum)


if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_fast(from_, to))
