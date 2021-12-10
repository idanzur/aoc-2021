#!/usr/bin/python3
import sys

file = './sample.txt' if 0 else './input.txt'

def calc_fuel(a, b):
    d = abs(a - b)
    return (1 + d) * d / 2


def part1():
    with open(file) as f:
        data = f.read()
    numbers = [int(i) for i in data.split(',')]
    min_d = sys.maxsize
    for i in range(min(numbers), max(numbers) + 1):
        s = sum([abs(n-i) for n in numbers])
        if s < min_d:
            min_d = s
    print(f'part1: {min_d}')

def part2():
    with open(file) as f:
        data = f.read()
    numbers = [int(i) for i in data.split(',')]
    min_d = sys.maxsize
    for i in range(min(numbers), max(numbers) + 1):
        s = sum([calc_fuel(n, i) for n in numbers])
        if s < min_d:
            min_d = s
    print(f'part2: {int(min_d)}')


if __name__  == '__main__':
    part2()
