import math

def optimal_summands(n):
    summands = []
    # write your code here
    r_n = int(math.sqrt(n))
    summands = [x for x in range(1, r_n + 1)]
    total_sum = (r_n * (r_n + 1) ) // 2
    for i in range(r_n + 1, n + 1):
        if total_sum + i > n :
            rem = n - total_sum
            summands[-1] = int(summands[-1] + rem)
            return summands
        else:
            total_sum += i
            summands.append(int(i))

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
