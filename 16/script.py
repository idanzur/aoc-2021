#!/usr/bin/python3
from dataclasses import dataclass
from typing import List
from pprint import pprint

file = './sample.txt' if 0 else './input.txt'

with open(file) as f:
    data = f.read()
buffer = bin(int(data, 16))[2:]
buffer = "0" * (4-len(buffer)%4) + buffer

def chop(size):
    global buffer
    res = buffer[:size]
    buffer = buffer[size:]
    return res

def chop_int(size):
    return int(chop(size), 2)

@dataclass
class Packet:
    type: int
    version: int
    sub_packets: List['Packet'] = None
    payload: int = None


def parse():
    if not buffer:
        return
    p_version = chop_int(3)
    p_type = chop_int(3)
    if p_type == 4:
        p_payload = ""
        while True:
            last = chop_int(1)
            chunck = chop(4)
            p_payload += chunck
            if last == 0:
                break
        p_payload = int(p_payload, 2)
        return Packet(type=p_type, version=p_version, payload=p_payload)

    len_type_id = chop_int(1)
    if len_type_id == 1:
        sub_packet_count = chop_int(11)
        sub_packets = [parse() for _ in range(sub_packet_count)]
    else:
        sub_packet_len = chop_int(15)
        target_len = len(buffer) - sub_packet_len
        sub_packets = []
        while target_len != len(buffer):
            sub_packets.append(parse())
    return Packet(type=p_type, version=p_version, sub_packets=sub_packets)

def sum_versions(root:Packet):
    if root.type == 4:
        return root.version
    return root.version + sum([sum_versions(p) for p in root.sub_packets ])


def part1():
    root = parse()
    res = sum_versions(root)
    print(f'part1: {res}')

def part2():
    pass

if __name__  == '__main__':
    part1()
