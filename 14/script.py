#!/usr/bin/python3
import re
from collections import Counter, defaultdict
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
    template, data = data.split('\n\n')
    translate = {}
    for row in data.split('\n'):
        src, insert = row.split(' -> ')
        new_1 = src[0] + insert
        new_2 = insert + src[1]
        translate[src] = [new_1, new_2]
    
    res = defaultdict(int)
    for i in range(0, len(template), 2):
        seg = template[i: i+2]
        if seg in translate:
            res[seg] += 1
    for _ in range(10):
        temp_res = {}
        for key in res:
            t1, t2= translate[key] 
            temp_res[t1] = res.get(t1, 0) + res[key]
            temp_res[t2] = res.get(t2, 0) + res[key]
        res = defaultdict(int, temp_res)
    
    pprint(temp_res)


    # with open('grath.dot', 'w') as f:
    #     f.write(dot)
    # os.system("dot -Tpng grath.dot  > out.png")
    

if __name__  == '__main__':
    part2()
