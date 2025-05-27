def change(money):
    # write your code here
    total_count = 0
    
    if money >= 10:
        total_count += money // 10
        money = money % 10

    if money >= 5:
        total_count += money // 5
        money = money % 5 
        
    return total_count + money


if __name__ == '__main__':
    m = int(input())
    print(change(m))
