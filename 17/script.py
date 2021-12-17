#!/usr/bin/python3

file = './sample.txt' if 0 else './input.txt'

def is_valid_y(v0, target_y):
    start = 0
    while True:
        start += v0
        v0 -= 1
        if start < target_y[0]:
            return False
        if target_y[0] <= start <= target_y[1]:
            return True

def calc_height(vy):
    return int((1 + vy) * vy / 2)

def load_data():
    with open(file) as f:
        data = f.read()
    target_x, target_y = data.split(',')
    target_x = tuple(map(int, target_x.split('..')))
    target_y = tuple(map(int, target_y.split('..')))
    return target_x, target_y

def part1():
    _, target_y = load_data()
    max_vy = 0
    for vy in range(1000):
        if is_valid_y(vy, target_y):
            max_vy = vy
    res = calc_height(max_vy)
    print(f'part1: {res}')


def is_valid_x(v0, target_x):
    start = 0
    while True:
        start += v0
        v0 -= 1
        if start > target_x[1]:
            return False
        if target_x[0] <= start <= target_x[1]:
            return True
        if v0 == 0:
            return False

def hit(vx, vy, target_x, target_y):
    start_x = start_y = 0
    while True:
        start_x += vx
        start_y += vy
        vx = max(vx - 1, 0)
        vy -= 1
        if start_x > target_x[1]:
            return False
        if start_y < target_y[0]:
            return False
        if target_x[0] <= start_x <= target_x[1] and target_y[0] <= start_y <= target_y[1]:
            return True


def part2():
    target_x, target_y = load_data()
    vy_opts = [ vy for vy in range(-1000 ,1000) if is_valid_y(vy, target_y)]
    vx_opts = [ vx for vx in range(1, 1000) if is_valid_x(vx, target_x)]

    count = 0
    for vx in vx_opts:
        for vy in vy_opts:
            if hit(vx, vy, target_x, target_y):
                count += 1 
    print(f'part2: {count}')

if __name__  == '__main__':
    part1()
    part2()
