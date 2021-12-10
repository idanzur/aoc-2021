#!/usr/bin/python3
from abc import abstractproperty
from pprint import pprint
import sys
from collections import defaultdict
from functools import reduce
from operator import mul
file = './sample.txt' if 0 else './input.txt'


def get_neighbors(x, y, mat):
    height = len(mat)
    width = len(mat[0])
    left = mat[y][x-1] if x-1 >= 0 else sys.maxsize
    right = mat[y][x+1] if x + 1 < width else sys.maxsize
    above = mat[y-1][x] if y - 1 >= 0 else sys.maxsize
    below = mat[y+1][x] if y + 1 < height else sys.maxsize
    return left, right, above, below

def is_low(x ,y, mat):
    left, right, above, below = get_neighbors(x, y, mat)
    val = mat[y][x]
    return val < left and val < right and val < above and val < below


def find_low(x, y, mat):
    left, right, above, below = get_neighbors(x, y, mat)
    if left < right and left < above and left < below:
        x = x - 1
    elif right < above and right < below:
        x = x + 1
    elif above < below:
        y = y - 1
    else:
        y = y + 1
    if is_low(x, y, mat):
        return x, y
    return find_low(x, y, mat)

def part1():
    with open(file) as f:
        data = f.read()
    mat = []
    for row in data.splitlines():
        mat.append([int(i) for i in row])
    
    res = 0
    for y, row in enumerate(mat):
        for x, val in enumerate(row):
            if is_low(x, y, mat):
                res += val + 1
    print(f'part1: {res}')

def part2():
    with open(file) as f:
        data = f.read()
    mat = []
    for row in data.splitlines():
        mat.append([int(i) for i in row])
    
    res = defaultdict(int)
    for y, row in enumerate(mat):
        for x, val in enumerate(row):
            if val == 9:
                continue
            if is_low(x, y, mat):
                res[(x,y)] += 1
            else:
                pos = find_low(x, y, mat)
                res[pos] += 1
    top_values = sorted(res.values())[-3:]
    ans = reduce(mul, top_values)
    print(f'part2: {ans}')

if __name__  == '__main__':
    part2()
