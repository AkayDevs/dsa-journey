from sys import stdin

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def optimal_value(capacity, weights, values):

    items_array = []
    n = len(weights)
    for i in range(n):
        items_array.append(Item(values[i], weights[i]))
    
    items_array.sort(key=lambda x: x.value/x.weight, reverse=True)

    cur_weight, cur_value = 0, 0
    for i in range(n):
        rem_weight = capacity - cur_weight
        if items_array[i].weight > rem_weight:
            cur_value += rem_weight * (items_array[i].value / items_array[i].weight)
            break
        else:
            cur_value += items_array[i].value
            cur_weight += items_array[i].weight

    return cur_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
