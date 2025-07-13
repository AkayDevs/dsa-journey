# Print this pattern
# 1
# 1  2
# 1  2  3
# 1  2  3  4
# 1  2  3  4  5

def print_pattern(num : int):
    for i in range(num):
        for j in range(i + 1):
            print(j + 1, end=" ")

        print()

if __name__ == "__main__":
    n = int(input())
    print_pattern(n)