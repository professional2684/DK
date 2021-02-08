# -*- coding: utf-8 -*-
def displayPathtoPrincess(n,grid):
    steps = []
    for i in range(len(grid)):
        if grid[i].find('m') >= 0:
            botloc = [i, grid[i].find('m')]
        if grid[i].find('p') >= 0:
            princessloc = [i, grid[i].find('p')]
    print(botloc, princessloc)
    # row and col check
    rw = botloc[0] - princessloc[0] # 0 same row, >0 next rows, < 0 previous rows
    cl = botloc[1] - princessloc[1] # 0 same col, >0 next cols, < 0 previous cols
    print(rw, cl)
    if rw > 0:
        for _ in range(rw):
            steps.append('DOWN')
    elif rw < 0:
        for _ in range(-1 * rw):
            steps.append('UP')
    if cl > 0:
        for _ in range(cl):
            steps.append('RIGHT')
    elif cl < 0:
        for _ in range(-1 * cl):
            steps.append('LEFT')
    for val in steps:
        print(val)
        
    
if __name__ == '__main__':
    # m = int(input())
    grid = ['---','-m-','p--'] 
    # for i in range(0, m): 
    #     grid.append(input().strip())
    
    displayPathtoPrincess(3,grid)
