#!/usr/bin/python3
import math
from copy import deepcopy

file = './sample.txt' if 0 else './input.txt'


class Reducer:
    def __init__(self, number):
        self.number = number
        self.path = None
        self.found = False

    def reduce(self):
        while self.explode() or self.split():
            self.path = None
            self.found = False
        return self.number

    def explode(self):
        self.find_explode(self.number, 0, [])
        if self.path:
            left_item, right_item = self.get_at(self.path)
            if right_path := self.find_near_number(0):
                self.add_at(right_path, right_item)
            if left_path := self.find_near_number(1):
                self.add_at(left_path, left_item)
            self.modify_at(self.path, 0)

        return bool(self.path)

    def find_explode(self, number, n, path):
        if type(number[0]) is int and type(number[1]) is int:
            if n == 4:
                self.found = True
                self.path = path
            return
        for i, item in enumerate(number):
            if self.found:
                return
            if type(item) is list:
                self.find_explode(item, n + 1, path + [i])

    def find_near_number(self, dir):
        path = self.path
        temp = self.number
        if dir not in path:
            return
        last_pos = len(path) - path[::-1].index(dir) - 1
        start_path = path[: last_pos] + [1-dir]

        temp = self.get_at(start_path)

        while temp != []:
            if type(temp) is int:
                return start_path
            start_path.append(dir)
            temp = temp[dir]

    def split(self):
        self.find_split(self.number, [])
        if self.path:
            item = self.get_at(self.path)
            self.modify_at(self.path, [item//2, math.ceil(item/2)])
        return bool(self.path)

    def find_split(self, number, path):
        for i, item in enumerate(number):
            if self.found:
                return
            if type(item) is list:
                self.find_split(item, path + [i])
            elif item >= 10:
                self.found = True
                self.path = path + [i]

    def modify_at(self, path, val):
        temp = self.get_at(path[:-1])
        temp[path[-1]] = val

    def add_at(self, path, val):
        temp = self.get_at(path[:-1])
        temp[path[-1]] += val

    def get_at(self, path):
        temp = self.number
        for i in path:
            temp = temp[i]
        return temp


def magnitude(number):
    if type(number) is int:
        return number
    return 3 * magnitude(number[0]) + 2 * magnitude(number[1])


def load_data():
    with open(file) as f:
        data = f.read()
    return list(map(eval, data.splitlines()))


def part1():
    rows = load_data()
    start = rows[0]
    for row in rows[1:]:
        start = Reducer([start, row]).reduce()
    ans = magnitude(start)
    print(f'part1: {ans}')


def part2():
    rows = load_data()
    max_mag = 0
    for a in rows:
        for b in rows:
            if a != b:
                calc = Reducer([deepcopy(a), deepcopy(b)]).reduce()
                max_mag = max(magnitude(calc), max_mag)
    print(f'part2: {max_mag}')


if __name__ == '__main__':
    part1()
    part2()
