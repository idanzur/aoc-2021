#!/usr/bin/python3
from typing import List
from math import pow
from itertools import permutations, combinations

file = './sample.txt' if 0 else './input.txt'


def distance(p1: tuple, p2: tuple) -> float:
    return sum([pow(a-b, 2) for a, b in zip(p1, p2)])


def get_distances(scanner: List[tuple]) -> dict:
    distances = {}
    for p1 in scanner:
        for p2 in scanner:
            if p1 is not p2:
                distances[distance(p1, p2)] = tuple(sorted([p1, p2]))
    return distances


def intersect_distances(d1: dict, d2: dict):
    res = []
    for k, v in d1.items():
        if k in d2:
            res.append([v, d2[k]])
    return res


def gen_views():
    options = []
    for x, y, z in permutations([0, 1, 2]):
        for i in range(8):
            t = [1, 1, 1]
            if i & 1:
                t[0] = -t[0]
            if i & 2:
                t[1] = -t[1]
            if i & 4:
                t[2] = -t[2]
            options.append([(x, y, z), t])
    return options


def translate_point(point, view):
    pos, dir = view
    x = point[pos[0]] * dir[0]
    y = point[pos[1]] * dir[1]
    z = point[pos[2]] * dir[2]
    return (x, y, z)


def translate_scanner(s, view):
    return [translate_point(p, view) for p in s]


def move_scanner(s, diff):
    return [tuple([p_+d_ for p_, d_ in zip(p, diff)]) for p in s]


def try_combine(s1, s2, p1, p2s):
    views = gen_views()
    _s1 = set(s1)
    for view in views:
        _s2 = translate_scanner(s2, view)
        for p2 in p2s:
            p2 = translate_point(p2, view)
            diff = tuple([p_-d_ for p_, d_ in zip(p1, p2)])
            __s2 = move_scanner(_s2, diff)
            ans = len(_s1 & set(__s2))
            if ans >= 12:
                return __s2

    return False


def combine(scanners, distances):
    for d1, d2 in combinations(distances, 2):
        i1 = distances.index(d1)
        i2 = distances.index(d2)
        intersect = intersect_distances(d1, d2)
        if len(intersect) >= 66:
            for inter in intersect:
                res = try_combine(
                    scanners[i1], scanners[i2], inter[0][0], inter[1])
                if res:
                    scanners[i1] = list(set(res) | set(scanners[i1]))
                    distances[i1] = d1 | get_distances(res)
                    scanners.pop(i2)
                    distances.pop(i2)
                    return scanners, distances


def part1():
    with open(file) as f:
        data = f.read()
    scanners = []
    for chunck in data.split('\n\n'):
        points = []
        for row in chunck.splitlines()[1:]:
            points.append(tuple(map(int, row.split(','))))
        scanners.append(points)

    distances = [get_distances(s) for s in scanners]
    while len(scanners) > 1:
        scanners, distances = combine(scanners, distances)

    ans = len(scanners[0])
    print(f'part1: {ans}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()
