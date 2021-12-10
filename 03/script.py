#!/usr/bin/python3

file = "./sample.txt" if 0 else "./input.txt"
def part1():
    with open(file) as f:
        nums = f.read().splitlines()
    gamma = ""
    size = len(nums[0])
    for i in range(size):
        t = [n[i] for n in nums]
        if t.count("1") > t.count("0"):
            gamma += "1"
        else:
            gamma += "0"
    gamma = int(gamma, 2)
    epsilon = ~gamma & (2**size-1)
    print(f'part 1: {gamma * epsilon}')


def part2():
    with open(file) as f:
        nums = f.read().splitlines()
    size = len(nums[0])
    for i in range(size):
        ones = []
        zeros = []
        for n in nums:
            if n[i] == '0':
                zeros.append(n)
            else:
                ones.append(n)
        if len(ones) >= len(zeros):
            nums = ones
        else:
            nums = zeros
        if len(nums) == 1:
            break
    oxygen = int(nums[0], 2)
    with open(file) as f:
        nums = f.read().splitlines()
    for i in range(size):
        ones = []
        zeros = []
        for n in nums:
            if n[i] == '0':
                zeros.append(n)
            else:
                ones.append(n)
        if len(ones) < len(zeros):
            nums = ones
        else:
            nums = zeros
        if len(nums) == 1:
            break
    co2 = int(nums[0], 2)
    print(f'part 2: {oxygen * co2}')


if __name__ == '__main__':
    part2()