#!/usr/bin/python3
import re
from collections import Counter
from pprint import pprint
import os

file = './sample.txt' if 1 else './input.txt'

def part1():
    with open(file) as f:
        data = f.read()
    template, data = data.split('\n\n')
    rules = []
    for row in data.split('\n'):
        rules.append(row.split(' -> '))

    for _ in range(10):
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
    with open(file) as f:
        data = f.read()
    data = data.split('\n\n')[1]
    dot = 'digraph {\n'
    for row in data.split('\n'):
        src, insert = row.split(' -> ')
        new_1 = src[0] + insert
        new_2 = insert + src[1]
        dot += f'  {src} -> {{{new_1} {new_2}}}\n'
    dot += '}'

    with open('grath.dot', 'w') as f:
        f.write(dot)
    os.system("dot -Tpng grath.dot  > out.png")
    

if __name__  == '__main__':
    part2()
