#!/usr/bin/python3
from os import close


file = './sample.txt' if 0 else './input.txt'

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
open_chars = '([{<'
close_chars = ')]}>'

def part1():
    with open(file) as f:
        data = f.read()
    res = 0
    for row in data.splitlines():
        stack = []
        for c in row:
            if c in open_chars:
                stack.insert(0, c)
            else:
                val = stack.pop(0)
                if not open_chars.index(val) == close_chars.index(c):
                    res += score[c]
                    break
    print(f'part1: {res}')

def part2():
    with open(file) as f:
        data = f.read()
    ans = []
    for row in data.splitlines():
        stack = []
        for c in row:
            if c in open_chars:
                stack.insert(0, close_chars[open_chars.index(c)])
            else:
                val = stack.pop(0)
                if val != c:
                    stack = []
                    break
        if stack:
            res = 0
            for val in stack:
                res = res * 5 + close_chars.index(val) + 1
            ans.append(res)
    index = (len(ans)-1)//2
    ans = sorted(ans)
    print(f'part2: {ans[index]}')

if __name__  == '__main__':
    part2()
