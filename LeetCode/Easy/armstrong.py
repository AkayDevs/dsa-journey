# Check whether a number is an Armstrong number. eg below:
# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153
import math

def check_armstrong(num : int):
    inp_str = str(num)
    total_sum = 0
    n = len(inp_str)
    for i in range(n):
        total_sum += math.pow(int(inp_str[i]), n)


    print(total_sum)
    if total_sum == num:
        return True
    
    return False




if __name__ == "__main__":
    n = int(input())
    print(check_armstrong(n))