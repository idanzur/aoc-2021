#!/usr/bin/python3

import re
import math

file = './sample.txt' if 0 else './input.txt'
size = 1000

def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell:
                print(cell, end='')
            else:
                print('.', end='')
        print()

def count_points(grid):
    s = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                s += 1
    return s

def draw_line(grid, x1, y1, x2, y2):
    dx = x1 - x2
    step_x = int(dx/abs(dx)) if x1 != x2 else 0
    dy = y1 - y2
    step_y = int(dy/abs(dy)) if y1 != y2 else 0
    for i in range(max(abs(dx), abs(dy))+ 1):
        new_x = x2 + step_x * i
        new_y = y2 + step_y * i
        grid[new_y][new_x] += 1
def part1():
    with open(file) as f:
        data = f.read()
    rows = re.findall('(\d+),(\d+) \-> (\d+),(\d+)', data)
    grid = [[0 for j in range(size)] for i in  range(size)]
    for nums in rows:
        x1, y1, x2, y2 = [int(n) for n in nums]
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                grid[i][x1] += 1
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][i] += 1

    # print_grid(grid)
    print(f'part1: {count_points(grid)}')

def part2():
    with open(file) as f:
        data = f.read()
    rows = re.findall('(\d+),(\d+) \-> (\d+),(\d+)', data)
    grid = [[0 for j in range(size)] for i in  range(size)]
    for nums in rows:
        x1, y1, x2, y2 = [int(n) for n in nums]
        draw_line(grid, x1, y1, x2, y2)
    # print_grid(grid)
    print(f'part2: {count_points(grid)}')


if __name__  == '__main__':
    part2()
