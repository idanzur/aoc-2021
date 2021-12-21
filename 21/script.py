#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'


def add(player, value):
    player += value
    while player > 10:
        player -= 10
    return player


def part1():
    with open(file) as f:
        data = f.read()
    p1, p2 = data.split(',')
    p1 = int(p1)
    p2 = int(p2)
    score_1 = score_2 = 0

    dice = 0
    while score_1 < 1000 and score_2 < 1000:
        for _ in range(3):
            dice += 1
            p1 = add(p1, dice)
        score_1 += p1
        if score_1 >= 1000:
            break
        for _ in range(3):
            dice += 1
            p2 = add(p2, dice)
        score_2 += p2

    res = min(score_1, score_2) * dice
    print(f'part1: {res}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()
