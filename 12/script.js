#!/usr/bin/env node
const fs = require('fs');

const file = 0 ? './sample.txt' : './input.txt';

class Cave {
    constructor(name) {
        this.name = name;
        this.paths = [];
        this.lower = name.toLowerCase() === name;
    }
    toString() {
        return this.name;
    }
}
function loadData() {
    const data = fs.readFileSync(file).toString();
    const caves = {};
    data.split('\n').forEach(line => {
        const [nameA, nameB] = line.split('-');
        const caveA = nameA in caves ? caves[nameA] : new Cave(nameA);
        const caveB = nameB in caves ? caves[nameB] : new Cave(nameB);
        caveA.paths.push(caveB);
        caveB.paths.push(caveA);
        caves[nameA] = caveA;
        caves[nameB] = caveB;
    })
    return caves.start;
}

const lookup = {}
function loadData2() {
    const data = fs.readFileSync(file).toString();
    data.split('\n').forEach(line => {
        const [nameA, nameB] = line.split('-');
        const caveA = nameA in lookup ? lookup[nameA] : [];
        const caveB = nameB in lookup ? lookup[nameB] : [];
        caveA.push(nameB);
        caveB.push(nameA);
        lookup[nameA] = caveA;
        lookup[nameB] = caveB;
    })
}


function findPath(visited, paths = new Set()) {
    const start = visited[visited.length - 1];
    if (start.name === 'end') {
        paths.add(visited.toString());
        return;
    }
    for (const cave of start.paths)
        if (!cave.lower || visited.indexOf(cave) === -1)
            findPath([...visited, cave], paths)
    return paths.size;
}

function part1() {
    const start = loadData();
    const res = findPath([start]);
    console.log(`part1: ${res}`);
}

function findPath2(visited, paths = new Set(), twice = false) {
    const start = visited[visited.length - 1];
    if (start.name === 'end') {
        paths.add(visited.toString());
        return;
    }

    for (const cave of start.paths) {
        if (cave.name === 'start')
            continue;
        if (cave.lower) {
            if (twice) {
                if (visited.indexOf(cave) === -1) {
                    findPath2([...visited, cave], paths, twice);
                }
            } else {
                findPath2([...visited, cave], paths, visited.indexOf(cave) > -1);
            }
        } else {
            findPath2([...visited, cave], paths, twice);
        }
    }
    return paths.size;
}

function findPath25(visited, paths = new Set(), twice = false) {
    const start = visited[visited.length - 1];
    if (start === 'end') {
        paths.add(visited.toString());
        return;
    }
    for (const cave of lookup[start]) {
        if (cave === 'start')
            continue;
        if (cave.toLowerCase() === cave) {
            if (twice) {
                if (visited.indexOf(cave) === -1) {
                    findPath25([...visited, cave], paths, twice);
                }
            } else {
                findPath25([...visited, cave], paths, visited.indexOf(cave) > -1);
            }
        } else {
            findPath25([...visited, cave], paths, twice);
        }
    }
    return paths.size;
}

function part2() {
    const start = loadData();
    const res = findPath2([start]);
    console.log(`part2: ${res}`);
    // console.log(lookup);
}

// part1()
part2()