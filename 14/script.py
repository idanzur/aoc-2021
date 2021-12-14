#!/usr/bin/python3
import re
from collections import Counter
from pprint import pprint

file = './sample.txt' if 0 else './input.txt'

def part1():
    with open(file) as f:
        data = f.read()
    template, data = data.split('\n\n')
    rules = []
    for row in data.split('\n'):
        rules.append(row.split(' -> '))

    for _ in range(40):
        print(i)
        matches = []
        for pattern, val in rules:
            for match in re.finditer(f'(?={pattern})', template):
                # print(pattern, (match.start(), val))
                matches.append((match.start() + 1, val))
        
        matches.sort(reverse=True)
        # print(matches)
        for index, val in matches:
            template = template[:index] + val + template[index:]
    
    vals_counter = Counter(template)
    vals = vals_counter.values()
    max_val = max(vals)
    min_val = min(vals)
    res = max_val - min_val
    print(f'part1: {res}')


def part2():
    pass

if __name__  == '__main__':
    part1()
