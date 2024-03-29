#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'

def part1():
    with open(file) as f:
        data = f.read()
    pos = 0
    depth = 0
    for row in data.splitlines():
        cmd, x = row.split(' ')
        x = int(x)
        if cmd == 'forward':
            pos += x
        elif cmd == 'down':
            depth += x
        else:
            depth -= x
    
    print(f'part1: {pos * depth}')

def part2():
    with open(file) as f:
        data = f.read()
    pos = 0
    depth = 0
    aim = 0
    for row in data.splitlines():
        cmd, x = row.split(' ')
        x = int(x)
        if cmd == 'down':
            aim += x
        elif cmd == 'up':
            aim -= x
        else:
            pos += x
            depth += x * aim
    
    print(f'part2: {pos * depth}')


if __name__  == '__main__':
    part2()
