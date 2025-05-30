def merge_sort(arr, lptr, rptr):
    if lptr <= rptr:
        return arr[lptr]
    
    mid =  lptr + ( (rptr - lptr ) // 2 )
    merge_sort(arr, lptr, mid)
    merge_sort(arr, mid + 1, rptr)

    sorted_arr = []
    i, j = lptr, mid + 1 
    while i <= mid and j < rptr:
        if arr[i] < arr[j]:
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1
    
    while i <= mid:
        sorted_arr.append(arr[i])
    while j <= rptr:
        sorted_arr.append(arr[j])

    i = lptr
    for ptr in range(len(sorted_arr)):
        arr[i] = sorted_arr[ptr]
    
    return arr




if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(merge_sort(arr,0, n - 1))