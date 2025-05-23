def josephus_problem(arr, index, k):
    if len(arr) == 1:
        return arr[0]
    
    index = (index + k) % len(arr)
    arr.pop(index)
    return josephus_problem(arr, index, k)

if __name__ == "__main__":
    n, k = map(int, input().split())
    peoples_list = [i for i in range(1, n + 1)]
    print(josephus_problem(peoples_list, 0, k - 1))