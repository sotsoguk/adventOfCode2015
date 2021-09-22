import os
import numpy as np
from itertools import accumulate
from collections import namedtuple
import numpy as np
import time


def main():
    # input
    print(os.getcwd())
    day = "06"
    inputFile = f'../inputs/day{day}.txt'
    print(inputFile)
    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()

    
    start_time = time.time()
    
    # parse input
    Command = namedtuple('Command',['com','x1','y1','x2','y2'])
    commands = []
    
    for l in lines:
        
        x = l.split(' ')
        if x[0] == "toggle":
            p1 = x[1].split(',')
            p2 = x[3].split(',')
            c = Command(2,int(p1[0]),int(p1[1]),int(p2[0]),int(p2[1]))
        elif x[1] == "on":
            p1 = x[2].split(',')
            p2 = x[4].split(',')
            c = Command(1,int(p1[0]),int(p1[1]),int(p2[0]),int(p2[1]))
        else:
            p1 = x[2].split(',')
            p2 = x[4].split(',')
            c = Command(0,int(p1[0]),int(p1[1]),int(p2[0]),int(p2[1]))
        commands.append(c)
    

    # create grid
    grid = np.zeros((1000,1000),dtype=np.int16)
    grid2 = np.zeros((1000,1000),dtype=np.int32)
    
    for c in commands:
        # turn off / dec
        if c.com == 0:
            grid[c.x1:c.x2+1,c.y1:c.y2+1] = 0
            grid2[c.x1:c.x2+1,c.y1:c.y2+1] -=1
        # turn on / inc by 1
        elif c.com == 1:
            grid[c.x1:c.x2+1,c.y1:c.y2+1] = 1
            grid2[c.x1:c.x2+1,c.y1:c.y2+1] += 1
        # toggle / inc by 2
        else:
            grid[c.x1:c.x2+1,c.y1:c.y2+1] +=1 
            grid2[c.x1:c.x2+1,c.y1:c.y2+1] +=2 
        
        #grid2= np.clip(grid2,0,1000000)
        grid2[grid2 <0] = 0
        
    # toggle
    grid = np.mod(grid,2)
    part1 = np.concatenate(grid).sum()
    part2 = np.concatenate(grid2).sum()
    duration = int((time.time() - start_time) * 1000000)

    print(
        f"AoC 2015\nDay {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")



if __name__ == "__main__":
    main()
