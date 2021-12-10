#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'

def part1():
    with open(file) as f:
        data = f.read()
    total = [0] * 9
    for i in data.split(','):
        total[int(i)] += 1
    for _ in range(256):
        temp_total = [0] * 9
        temp_total[8] = total[0]
        temp_total[6] = total[0]
        for i in range(1, 9):
            temp_total[i-1] += total[i]
        total = temp_total
    print(f'part1: {sum(total)}')
def part2():
    pass

if __name__  == '__main__':
    part1()
