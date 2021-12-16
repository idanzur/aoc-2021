#!/usr/bin/python3
import sys
from pprint import pprint
from typing import List
import heapq

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


class Queue:
    def __init__(self) -> None:
        self.items = []

    def add(self, item):
        if item not in self.items:
            heapq.heappush(self.items, item)

    def pop(self):
        return heapq.heappop(self.items)

    def empty(self):
        return len(self.items) == 0


def get_neighbors(grid, x, y):
    size = len(grid)
    points = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(grid[j][i], i, j) for i, j in points if (0 <= i < size) and (0 <= j < size)]


def dijkstra(grid):
    size = len(grid)
    to_visit = Queue()
    to_visit.add((0, 0, 0))
    visited = [[0 for _ in range(size)] for _ in range(size)]
    costs = [[sys.maxsize for _ in range(size)] for _ in range(size)]
    costs[0][0] = 0
    while not to_visit.empty():
        _, cur_x, cur_y = to_visit.pop()
        visited[cur_y][cur_x] = 1
        neighbors = get_neighbors(grid, cur_x, cur_y)
        for n_w, n_x, n_y in neighbors:
            if not visited[n_y][n_x]:
                costs[n_y][n_x] = min(
                    costs[n_y][n_x],
                    costs[cur_y][cur_x] + n_w
                )
                to_visit.add((costs[n_y][n_x], n_x, n_y))

    return costs[-1][-1]


def part2():
    grid = load_data()
    grid = scale_grid(grid, 5)

    res = dijkstra(grid)
    print(f'part2: {res}')


if __name__ == '__main__':
    part1()
    part2()
