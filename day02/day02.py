import os
import numpy as np
from itertools import accumulate

import time


def main():
    # input
    print(os.getcwd())
    day = "02"
    inputFile = f'../inputs/day{day}.txt'
    print(inputFile)
    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    print(lines[0].split('x'))
    input_un = [list(map(int, l.split('x'))) for l in lines]
    input = [sorted(l) for l in input_un]
    print(input[0:3])
    start_time = time.time()
    def f1(a, b, c): return 2*(a*b+a*c+b*c)+a*b
    def f2(a, b, c): return 2*(a+b)+a*b*c
    #p = list(map(lambda x: 2*(x[0]*x[1]+x[0]*x[2]+x[1]*x[2])+x[0]*x[1],input))
    #p2 = list(map(lambda x: 2*(x[0]+x[1])+x[0]*x[1]*x[2],input))
    p1 = [f1(*i) for i in input]
    p2 = [f2(*i) for i in input]
    # print(sum(p3))

    part1 = sum(p1)
    part2 = sum(p2)

    # part1

    duration = int((time.time() - start_time) * 1000000)

    print(
        f"AoC 2015\nDay {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")


if __name__ == "__main__":
    main()
