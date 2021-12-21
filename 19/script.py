#!/usr/bin/python3
from typing import List, Dict, Tuple, TypeVar
from math import comb, pow, sqrt
from pprint import pprint
from collections import Counter
from itertools import permutations

file = './sample.txt' if 1 else './input.txt'


def distance(p1: tuple, p2: tuple) -> float:
    return sqrt(sum([pow(a-b, 2) for a, b in zip(p1, p2)]))


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


def diff(p1, p2):
    return [a-b for a, b in zip(p1, p2)]


def transform(p):
    options = []
    for x, y, z in permutations(p):
        for i in range(8):
            if i & 1:
                x = -x
            if i & 2:
                y = -y
            if i & 4:
                z = -z
            options.append((x, y, z))
    return options


def combine(inter):
    (p1, p2), (p3, p4) = inter
    diff_a = diff(p1, p2)
    # diff_b = diff(p2, p3)
    # print(diff_a, diff_b)
    for opt3, opt4 in zip(transform(p3), transform(p4)):
        print(diff_a == diff(opt4, opt3))


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



def try_combine(s1, s2):
    views = gen_views()
    for view in views:
        

def part1():
    with open(file) as f:
        data = f.read()
    scanners = []
    for chunck in data.split('\n\n'):
        points = []
        for row in chunck.splitlines()[1:]:
            points.append(tuple(map(int, row.split(','))))
        scanners.append(points)

    s0 = scanners[0]
    for s in scanners[1:]:
        try_combine(s0, s)

    # distances = [get_distances(s) for s in scanners]
    # d_start = distances[0]
    # for i, d in enumerate(distances[1:]):
    #     intersections = intersect_distances(d_start, d)
    #     if len(intersections) >= 66:
    #         print(combine(intersections[0]))
    # all_inter = set()
    # for i, d1 in enumerate(distances):
    #     for j, d2 in enumerate(distances):
    #         if i != j:
    #             intersections = intersect_distances(d1, d2)
    #             if len(intersections) >= 66:
    #                 all_inter.add(tuple(sorted([i, j])))

    # pprint(len(all_inter))


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()
