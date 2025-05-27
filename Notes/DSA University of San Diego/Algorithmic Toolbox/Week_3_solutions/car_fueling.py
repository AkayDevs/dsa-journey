from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    stops.insert(0, 0)
    n = len(stops)
    current_position, ptr, count = 0, 1, 0
    while ptr < n:
        delta = stops[ptr] - stops[current_position]
        if delta <= tank:
            ptr += 1
        else:
            if current_position == ptr - 1:
                return -1
            count += 1
            current_position = ptr - 1
    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
