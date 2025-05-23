def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_optimised(n):
    if n <= 1:
        return n
    
    f_list = [0] * (n + 1)
    f_list[1] = 1
    for i in range(2, n+1):
        f_list[i] = f_list[i - 1] + f_list[i - 2]
    return f_list[n - 1]
    


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_optimised(input_n))
