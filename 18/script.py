#!/usr/bin/python3
import math
from copy import deepcopy

file = './sample.txt' if 0 else './input.txt'

found = False
explode_path = None
def find_explode(query):
    global found, explode_path
    found = False
    explode_path = None
    def inner(query, n, path):
        global found, explode_path
        if type(query[0]) is int and type(query[1]) is int:
            if n == 4:
                found = True
                explode_path = path
            return
        for i, item in enumerate(query):
            if type(item) is list and not found:
                inner(item, n + 1, path + [i])
    
    return inner(query, 0, [])


def find_number(query, path, dir):
    if dir not in path:
        return
    last_pos = len(path) - path[::-1].index(dir) - 1
    start_path = path[: last_pos] + [1-dir]
    for i in start_path:
        query = query[i]

    while query != []:
        if type(query) is int:
            return start_path
        start_path.append(dir)
        query = query[dir]

def modify_at(query, path, val):
    for i in path[:-1]:
        query = query[i]
    query[path[-1]] = val

def add_at(query, path, val):
    for i in path[:-1]:
        query = query[i]
    query[path[-1]] += val

def get_at(query, path):
    for i in path:
        query = query[i]
    return query


found = False
split_path = None
def find_split(query):
    global found, split_path
    found = False
    split_path = None
    def inner(query, path):
        global found, split_path
        for i, item in enumerate(query):
            if found:
                continue
            if type(item) is list:
                inner(item, path + [i])
            elif item >= 10:
                found = True
                split_path = path + [i]
    
    return inner(query, [])


def explode(query):
    LEFT = 1
    RIGHT = 0
    global explode_path
    find_explode(query)
    if explode_path:
        # print(f'{explode_path=}')
        left_item, right_item = get_at(query, explode_path)
        # print(f'[{left_item}, {right_item}]')
        right_path = find_number(query, explode_path, RIGHT)
        # print(f'{right_path=}')
        if right_path:
            add_at(query, right_path, right_item)
        left_path = find_number(query, explode_path, LEFT)
        # print(f'{left_path=}')
        if left_path:
            add_at(query, left_path, left_item)  
        modify_at(query, explode_path, 0)
        # print(f'{query=}')
    
    return bool(explode_path)

def split(query):
    find_split(query)
    if split_path:
        # print(f'{split_path=}')
        item = get_at(query, split_path)
        # print(item)
        modify_at(query, split_path, [item//2, math.ceil(item/2)])
        # print(f'{query=}')
    return bool(split_path)

def calculate(query):
    # print(f'{query=}')
    exploded = splited = True
    while exploded or splited:
        exploded = splited = True
        while exploded:
            exploded = explode(query)
        splited = split(query)
    
    # print(f'{query=}')
    return query

def magnitude(query):
    if type(query) is int:
        return query
    return 3 * magnitude(query[0]) + 2 * magnitude(query[1])
def part1():
    global explode_path, split_path
    with open(file) as f:
        data = f.read()
    
    rows = list(map(eval, data.splitlines()))
    start = rows[0]
    for row in rows[1:]:
        start = calculate([start, row])
    
    ans = (magnitude(start))
    print(f'part1: {ans}')


def part2():
    global explode_path, split_path
    with open(file) as f:
        data = f.read()
    
    rows = list(map(eval, data.splitlines()))
    max_mag = 0
    for a in rows:
        for b in rows:
            if a != b:
                calc = calculate([deepcopy(a), deepcopy(b)])
                new_mag = magnitude(calc)
                if new_mag > max_mag:
                    max_mag = new_mag
    print(f'part2: {max_mag}')
if __name__  == '__main__':
    # part1()
    part2()
