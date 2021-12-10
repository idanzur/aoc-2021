#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'

def part1():
    with open(file) as f:
        data = f.read()
    s = 0
    for row in data.splitlines():
        out = row.split(' | ')[1]
        for n in out.split(' '):
            if len(n) in [2, 3, 4, 7]:
                s += 1
    print(f'part1: {s}')

def print_correct(correct):
    for i, v in enumerate(correct):
        print(f'{i}: {v}')

def b_in_a(a, b):
    return set(a) & set(b) == set(b)
def part2():
    with open(file) as f:
        data = f.read()
    s = 0
    for row in data.splitlines():
        correct = [0] * 10
        digits, out = row.split(' | ')
        out = out.split(' ')
        digits = digits.split(' ')
        for d in digits[::-1]:
            if len(d) == 2:
                correct[1] = d
                digits.remove(d)
            elif len(d) == 3:
                correct[7] = d
                digits.remove(d)
            elif len(d) == 4:
                correct[4] = d
                digits.remove(d)
            elif len(d) == 7:
                correct[8] = d
                digits.remove(d)
        
        zero_six_nine = [n for n in digits if len(n) == 6]
        for n in zero_six_nine:
            if not b_in_a(n, correct[1]):
                correct[6] = n
                zero_six_nine.remove(n)
                break
        
        if b_in_a(zero_six_nine[0], correct[4]):
            correct[9] = zero_six_nine[0]
            correct[0] = zero_six_nine[1]
        else:
            correct[9] = zero_six_nine[1]
            correct[0] = zero_six_nine[0]      

        two_three_five = [n for n in digits if len(n) == 5]
        for n in two_three_five:
            if b_in_a(correct[6], n):
                correct[5] = n
                two_three_five.remove(n)

        if b_in_a(correct[9], two_three_five[0]):
            correct[3] = two_three_five[0]
            correct[2] = two_three_five[1]
        else:
            correct[3] = two_three_five[1]
            correct[2] = two_three_five[0]      

        res = ""
        for d in out:
            for i, n in enumerate(correct):
                if list(sorted(d)) == list(sorted(n)):
                    res += str(i)
                    break
        s += int(res)
    print(s)


if __name__  == '__main__':
    part2()
