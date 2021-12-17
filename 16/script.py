#!/usr/bin/python3
from dataclasses import dataclass
from typing import List
from functools import reduce
from operator import mul

file = './sample.txt' if 0 else './input.txt'


@dataclass
class Packet:
    type: int
    version: int
    sub_packets: List['Packet'] = None
    payload: int = None
    


class Parser:

    def __init__(self) -> None:
        with open(file) as f:
            data = f.read()
        self.buffer = bin(int(data, 16))[2:].zfill(len(data) * 4)

    def chop(self, size):
        res = self.buffer[:size]
        self.buffer = self.buffer[size:]
        return res

    def chop_int(self, size):
        return int(self.chop(size), 2)

    def parse(self):
        p_version = self.chop_int(3)
        p_type = self.chop_int(3)
        if p_type == 4:
            p_payload = ""
            while True:
                last = self.chop_int(1)
                chunck = self.chop(4)
                p_payload += chunck
                if last == 0:
                    break
            p_payload = int(p_payload, 2)
            return Packet(type=p_type, version=p_version, payload=p_payload)
        len_type_id = self.chop_int(1)
        if len_type_id == 1:
            sub_packet_count = self.chop_int(11)
            sub_packets = [self.parse() for _ in range(sub_packet_count)]
        else:
            sub_packet_len = self.chop_int(15)
            target_len = len(self.buffer) - sub_packet_len
            sub_packets = []
            while target_len != len(self.buffer):
                sub_packets.append(self.parse())

        return Packet(type=p_type, version=p_version, sub_packets=sub_packets)


def sum_versions(root: Packet):
    if root.type == 4:
        return root.version
    return root.version + sum([sum_versions(p) for p in root.sub_packets])


def calc(root: Packet):
    if root.type == 0:
        return sum(map(calc, root.sub_packets))
    if root.type == 1:
        return reduce(mul, map(calc, root.sub_packets))
    if root.type == 2:
        return min(map(calc, root.sub_packets))
    if root.type == 3:
        return max(map(calc, root.sub_packets))
    if root.type == 4:
        return root.payload
    if root.type == 5:
        return int(calc(root.sub_packets[0]) > calc(root.sub_packets[1]))
    if root.type == 6:
        return int(calc(root.sub_packets[0]) < calc(root.sub_packets[1]))
    if root.type == 7:
        return int(calc(root.sub_packets[0]) == calc(root.sub_packets[1]))


def part1():
    parser = Parser()
    root = parser.parse()
    res = sum_versions(root)
    print(f'part1: {res}')


def part2():
    parser = Parser()
    root = parser.parse()
    res = calc(root)
    print(f'part2: {res}')


if __name__ == '__main__':
    part1()
    part2()
