def solve(heights, n):
    max_area = 0
    i, j = 0, n - 1
    while i < j:
        cur_area = min(heights[i], heights[j]) * (j - i)
        if cur_area > max_area:
            max_area = cur_area

        if heights[i] < heights[j]:
            i += 1
        else :
            j -= 1

    return max_area
    


if __name__ == "__main__":
    n = int(input())
    heights = list(map(int, input().split()))
    print(solve(heights, n))