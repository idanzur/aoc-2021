#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'

def part1():
    with open(file) as f:
        data = f.read()
    numbers = [int(i) for i in data.splitlines()]
    res = sum([1 for a, b in zip(numbers, numbers[1:]) if b > a])
    print(f'part1: {res}')
    

def part2():
    with open(file) as f:
        data = f.read()
    numbers = [int(i) for i in data.splitlines()]
    res = sum([1 for a, b in zip(numbers, numbers[3:]) if b > a])
    print(f'part2: {res}')

if __name__  == '__main__':
    part2()
