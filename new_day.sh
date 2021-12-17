#!/bin/sh
set -xe

mkdir $1
cd $1
cat > script.py <<EOF
#!/usr/bin/python3
file = './sample.txt' if 1 else './input.txt'

def part1():
    with open(file) as f:
        data = f.read()

def part2():
    pass

if __name__  == '__main__':
    part1()
    # part2()
EOF

curl https://adventofcode.com/2021/day/$1/input -s --header "Cookie: session=$(cat ../session.txt)" -o input.txt
truncate -s-1 input.txt 
touch sample.txt

code .
