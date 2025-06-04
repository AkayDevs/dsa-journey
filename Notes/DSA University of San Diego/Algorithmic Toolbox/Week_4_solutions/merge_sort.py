def merge_sort(arr, lptr, rptr):
    if lptr >= rptr:
        return
    
    mid =  lptr + ( (rptr - lptr ) // 2 )

    merge_sort(arr, lptr, mid)
    merge_sort(arr, mid + 1, rptr)

    merge(arr, lptr, rptr, mid)


def merge(arr, lptr, rptr, mid):
    final_list = []

    i, j = lptr, mid + 1 
    while i <= mid and j <= rptr:
        if arr[i] < arr[j]:
            final_list.append(arr[i])
            i += 1
        else:
            final_list.append(arr[j])
            j += 1
    
    while i <= mid:
        final_list.append(arr[i])
        i += 1
    while j <= rptr:
        final_list.append(arr[j])
        j += 1

    for i in range(len(final_list)):
        arr[lptr + i] = final_list[i]

    return




if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, n - 1)
    print(arr)