import os
import numpy as np
from itertools import accumulate

import time
import hashlib


def main():
    # input
    print(os.getcwd())
    day = "04"
    #inputFile = f'../inputs/day{day}.txt'
    
    part1, part2 = 0, 0
    # with open(inputFile) as f:
    #     lines = f.read().splitlines()
    input = "iwrupvqb"
    start_time = time.time()
    
    #part1
    p1b,p2b = False, False
    i = 0
    while p1b == False or p2b == False:
        str2hash = input + str(i)
        result = hashlib.md5(str2hash.encode())    
        if p1b == False and result.hexdigest()[:5] == "00000":
            part1 = i
            p1b = True
            
        if result.hexdigest()[:6] == "000000":
            part2 = i
            p2b = True
        i += 1
    duration = int((time.time() - start_time) * 1000000)

    print(
        f"AoC 2015\nDay {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")



if __name__ == "__main__":
    main()
