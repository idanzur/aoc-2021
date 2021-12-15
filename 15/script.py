#!/usr/bin/python3
import sys
from pprint import pprint

file = './sample.txt' if 0 else './input.txt'


def calc_point_cost(cost, x, y):
    cost_up = cost_left = sys.maxsize
    if y > 0:
        cost_up = cost[y - 1][x]
    if x > 0:
        cost_left = cost[y][x - 1]
    return min(cost_left, cost_up)


def print_grid(grid):
    for row in grid:
        for val in row:
            print(f'{val: >2}', end=' ')
        print()


def load_data():
    with open(file) as f:
        data = f.read()
    grid = []
    for row in data.splitlines():
        grid.append([int(i) for i in row])
    return grid


def calc_cost(grid):
    size = len(grid)
    cost = [[0] * size for _ in range(size)]
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if y == 0 and x == 0:
                cost[y][x] = 0
            else:
                cost[y][x] = calc_point_cost(cost, x, y) + val

    return cost[-1][-1]


def scale_grid(grid, scale):
    size = len(grid)
    res = []
    for y in range(size * scale):
        t = []
        for x in range(size * scale):
            val = grid[y % size][x % size]
            add = (y // size) + (x // size)
            new_val = val + add
            if new_val > 9:
                new_val -= 9
            t.append(new_val)
        res.append(t)
    return res


def part1():
    grid = load_data()
    res = calc_cost(grid)
    print(f'part1: {res}')


def part2():
    grid = load_data()
    grid = scale_grid(grid, 5)
    # with open('./large_sample.txt') as f:
    #     data = f.read()
    # large = []
    # for row in data.splitlines():
    #     large.append([int(i) for i in row])

    # for i in range(25):
    #     for j in range(25):
    #         print(int(grid[i][j] == large[i][j]), end=' ')
    #     print()

    res = calc_cost(grid)
    print(f'part2: {res}')


if __name__ == '__main__':
    part1()
    part2()
