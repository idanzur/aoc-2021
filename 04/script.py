#!/usr/bin/python3

import re
from typing import List, Tuple
from dataclasses import dataclass


file = "./sample.txt" if 0 else "./input.txt"
CROSSED_FORMAT = '\033[1m{}\033[0m'

@dataclass
class Cell:
    val: int
    crossed: bool = False
    def __repr__(self) -> str:
        if self.crossed:
            val = f'{self.val: >3}' 
            return CROSSED_FORMAT.format(val)
        return f'{self.val: >3}'

class Board:
    SIZE = 5
    def __init__(self, numbers):
        self.cells = [Cell(val=n) for n in numbers]

    def mark(self, n):
        for cell in self.cells:
            if cell.val == n:
                cell.crossed = True
                break
    def is_win(self):
        for i in range(0, len(self.cells), self.SIZE):
            if all(map(lambda cell: cell.crossed, self.cells[i:i+self.SIZE])):
                return True
        for j in range(self.SIZE):
            won = True
            for i in range(self.SIZE):
                if not self.cells[i*self.SIZE + j].crossed:
                    won = False
                    break
            if won:
                return True
        return False

    def score(self):
        return sum([cell.val for cell in self.cells if not cell.crossed])
    
    def __repr__(self) -> str:
        res = ""
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                val = str(self.cells[i*self.SIZE +j])
                res += val
            res += '\n'
        return res

def mark_number(n, boards: List[Board]):
    for board in boards:
        board.mark(n)

def find_winner(boards: List[Board]) -> Board:
    for board in boards[::-1]:
        if board.is_win():
            return board

def remove_winners(boards: List[Board]):
    return [board for board in boards if not board.is_win()]

def load_data() -> Tuple[List[int], List[Board]]:
    with open(file) as f:
        data = f.read().split('\n\n')

    numbers = [int(i) for i in data[0].split(',')]
    boards = []
    for chunck in data[1:]:
        boards.append(Board([int(i) for i in re.findall('\d+', chunck)]))
    return numbers, boards


def part1():
    numbers, boards = load_data()
    for n in numbers:
        mark_number(n, boards) 
        winner = find_winner(boards)
        if winner:
            print(f'part1: {winner.score() * n}')
            break

def part2():
    numbers, boards = load_data()
    for n in numbers:
        mark_number(n, boards)
        if len(boards) > 1:
            boards = remove_winners(boards)
        else:
            winner = find_winner(boards)
            if winner:
                print(f'part2: {winner.score() * n}')
                break

if __name__ == '__main__':
    part1()
    part2()