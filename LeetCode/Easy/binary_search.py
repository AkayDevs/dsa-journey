# Input List: [1, 9, 5, 7, 3, 11, 13]
# Input Target: 5

from typing import List

def binary_serach(l: List[int], target: int, left: int, right: int):
    if right <= left:
        return -1
        
    m = (left + right) // 2
    if l[m][0] == target:
        return l[m][1]
    elif l[m][0] > target:
        return binary_serach(l, target, left, m)
    else :
        return binary_serach(l, target, m + 1, right)
    
    
if __name__ == "__main__":
    l = list(map(int, input().split()))
    target = int(input())
    new_l = []
    for i in range(len(l)):
        new_l.append((l[i], i))
        
    new_l.sort()
    print(binary_serach(new_l, target, 0, len(new_l)))

    
    