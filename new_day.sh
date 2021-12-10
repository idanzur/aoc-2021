#!/bin/sh
set -e

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
EOF

touch input.txt
touch sample.txt

code .
