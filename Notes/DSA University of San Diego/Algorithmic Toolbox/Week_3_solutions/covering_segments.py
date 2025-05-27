from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

def get_coords(segments):
    n = len(segments)
    segments.sort(key=lambda x: x.start)
    coords = []
    i, min_end = 0, 0
    while i < n:
        cur_min = segments[i].end
        i += 1
        while i < n and segments[i].start <= cur_min:
            cur_min = min(segments[i].end, cur_min)
            i += 1
        coords.append(cur_min)

    print(len(coords))
    c = " ".join(map(str, coords))
    print(c)
    return

        


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    get_coords(segments)
