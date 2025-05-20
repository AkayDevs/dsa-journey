def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)


def lcmOptimised(a, b):

    gcd_ab = gcd(a, b) if a >= b else gcd(b, a)
    return  ( a * b ) // gcd_ab




if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcmOptimised(a, b))

