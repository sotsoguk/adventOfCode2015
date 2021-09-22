import os
import numpy as np
from itertools import accumulate

import time


def main():
    # input
    print(os.getcwd())
    day = "03"
    inputFile = f'../inputs/day{day}.txt'
    print(inputFile)
    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()

    start_time = time.time()
    
    dir_dict = {'v': (0, -1), '^': (0, 1), '<': (-1, 0), '>': (1, 0)}
    commands = [dir_dict[c] for c in lines[0]]
    positions1 = [(0,0)]+list(zip(*map(accumulate,zip(*commands))))

    part1 = len(set(positions1))

    p2s =[(0,0)]+list(zip(*map(accumulate,zip(*commands[::2])))) 
    p2r =[(0,0)]+list(zip(*map(accumulate,zip(*commands[1::2])))) 
    # print(commands)
    part2 = len(set(p2s).union(set(p2r)))
    # part1

    duration = int((time.time() - start_time) * 1000000)

    print(
        f"AoC 2015\nDay {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")



if __name__ == "__main__":
    main()
