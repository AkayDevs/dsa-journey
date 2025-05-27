
def party_celebration_fast(ages, n):
    ages.sort()
    i , count = 0, 0

    while i < n: 
        min_index = i
        count += 1
        while i < n and ages[i] - ages[min_index] <= 2:
            i += 1

    return count




if __name__ == "__main__":
    n = int(input())
    ages = list(map(int, input().split()))
    print(party_celebration_fast(ages, n))