#!/usr/bin/python3

file = './sample.txt' if 0 else './input.txt'


def print_grid(grid):
    print('\n'.join([''.join(row) for row in grid]))


def combine(arr1, arr2):
    for y, (row1, row2) in enumerate(zip(arr1, arr2)):
        for x, (cell1, cell2) in enumerate(zip(row1, row2)):
            if cell1 == '#' or cell2 == '#':
                arr1[y][x] = '#'
    return arr1


def count_grid(grid):
    s = 0
    for row in grid:
        for cell in row:
            s += 1 if cell == '#' else 0
    return s


def part1():
    with open(file) as f:
        data = f.read()
    rows, instructions = data.split('\n\n')
    points = []
    max_x = max_y = 0
    for row in rows.split('\n'):
        x, y = row.split(',')
        x = int(x)
        y = int(y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        points.append((x, y))

    grid = [['.'] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in points:
        grid[y][x] = '#'

    for i, fold in enumerate(instructions.split('\n')):
        axis, index = fold.split(' ')[-1].split('=')
        index = int(index)
        if axis == 'y':
            a = grid[:index]
            b = grid[index+1::][::-1]
        else:
            a = []
            b = []
            for row in grid:
                a.append(row[:index])
                b.append(row[index+1:][::-1])

        grid = combine(a, b)
        if i == 0:
            print(f'part1: {count_grid(grid)}')
    print('part2:')
    print_grid(grid)

<<<<<<< HEAD

def part2():
    pass

=======
>>>>>>> db7cb44f917921de16f1efa4d5a25b087dc0a1db

if __name__ == '__main__':
    part1()
