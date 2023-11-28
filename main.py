import numpy as np
from numpy import random
from person import Person
from level import Level
from level import Type
from view import Settings, gameLoop, gameLoopSectionB

# global parameters
GRID_SIZE = 100


def main():
    p = 0.6
    levels_probs = [0, 0.25, 0.25, 0.25, 0.25]
    iterations = 500
    l = 3
    p, l, levels_probs, iterations = Settings(p, l, levels_probs, iterations)
    grid, people_sum = createGrid(p, levels_probs, l)
    rumour_spreader = chooseRumourSpreader(grid)
    rumour_spreader.isBeliever = True
    gameLoop(iterations, grid, iterationFunc, people_sum)


def createGrid(p, levels_probs, l):
    sum = 0
    # building grid of people
    temp_grid = random.choice([0, 4, 3, 2, 1],
                              size=(GRID_SIZE, GRID_SIZE),
                              p=[1 - p, p * (levels_probs[4]), p * (levels_probs[3]), p * (levels_probs[2]),
                                 p * (levels_probs[1])])
    grid = np.empty((GRID_SIZE, GRID_SIZE), dtype=Person)
    row, col = temp_grid.shape
    for i in range(row):
        for j in range(col):
            if temp_grid[i, j] == 0:
                grid[i, j] = None
            if temp_grid[i, j] == 1:
                grid[i, j] = Person(level=Level(Type.S1))
            elif temp_grid[i, j] == 2:
                grid[i, j] = Person(level=Level(Type.S2))
            elif temp_grid[i, j] == 3:
                grid[i, j] = Person(level=Level(Type.S3))
            elif temp_grid[i, j] == 4:
                grid[i, j] = Person(level=Level(Type.S4))
            if grid[i,j] != None:
                sum += 1
                grid[i,j].place = (i,j)     # delete
                grid[i,j].L = l

    # find all neighbors
    row, col = grid.shape
    for i in range(row):
        for j in range(col):
            if grid[i, j] != None:
                neighbors = []
                # 1
                if i - 1 >= 0 and j - 1 >= 0:
                    if grid[i - 1, j - 1] != None:
                        neighbors.append(grid[i - 1, j - 1])
                # 2
                if i - 1 >= 0:
                    if grid[i - 1, j] != None:
                        neighbors.append(grid[i - 1, j])
                # 3
                if i - 1 >= 0 and j + 1 <= GRID_SIZE - 1:
                    if grid[i - 1, j + 1] != None:
                        neighbors.append(grid[i - 1, j + 1])
                # 4
                if j - 1 >= 0:
                    if grid[i, j - 1] != None:
                        neighbors.append(grid[i, j - 1])
                # 5
                if j + 1 <= GRID_SIZE - 1:
                    if grid[i, j + 1] != None:
                        neighbors.append(grid[i, j + 1])
                # 6
                if i + 1 <= GRID_SIZE - 1 and j - 1 >= 0:
                    if grid[i + 1, j - 1] != None:
                        neighbors.append(grid[i + 1, j - 1])
                # 7
                if i + 1 <= GRID_SIZE - 1:
                    if grid[i + 1, j] != None:
                        neighbors.append(grid[i + 1, j])
                # 8
                if i + 1 <= GRID_SIZE - 1 and j + 1 <= GRID_SIZE - 1:
                    if grid[i + 1, j + 1] != None:
                        neighbors.append(grid[i + 1, j + 1])
                grid[i, j].neighbors = neighbors
    return grid, sum


def chooseRumourSpreader(grid):
    # choose a rumour spreader
    rumour_spreader = None
    while rumour_spreader == None:
        place = random.randint(low=0, high=GRID_SIZE, size=2)
        rumour_spreader = grid[place[0], place[1]]
    return rumour_spreader


def iterationFunc(grid):
    # rumour spreading
    for cell in grid.flatten():
        if cell is not None:
            cell.spread()
    # every cell decides if to believe
    for cell in grid.flatten():
        if cell is not None:
            cell.believe()
    return grid


'''
Section B functions
'''


def mainSectionB():
    p = 0.6
    levels_probs = [0, 0.25, 0.25, 0.25, 0.25]
    iterations = 500
    l = 3
    p, l, levels_probs, iterations = Settings(p, l, levels_probs, iterations)
    grid, people_sum = createGridSectionB(p, levels_probs, l)
    rumour_spreader = chooseRumourSpreaderSectionB(grid)
    rumour_spreader.isBeliever = True
    gameLoopSectionB(iterations, grid, iterationFunc, people_sum)


def createGridSectionB(p, levels_probs, l):
    sum = 0
    # building grid of people
    grid = np.empty((GRID_SIZE, GRID_SIZE), dtype=Person)
    row, col = grid.shape
    for i in range(row):
        for j in range(col):
            choice = random.choice([0,1],p=[1-p, p])
            if choice == 0 and i != 50 and j != 50:
                grid[i, j] = None
            else:
                if i <= 12 or j <= 12 or i>= 88 or j>= 88:
                    grid[i, j] = Person(level=Level(Type.S4))
                elif i <= 25 or j <= 25 or i>= 75 or j>= 75:
                    grid[i, j] = Person(level=Level(Type.S3))
                elif i <= 37 or j <= 37 or i>= 63 or j>= 63:
                    grid[i, j] = Person(level=Level(Type.S2))
                else:
                    grid[i, j] = Person(level=Level(Type.S1))
                sum += 1
                # grid[i,j].place = (i,j)     # delete
                grid[i,j].L = l
    # find all neighbors
    row, col = grid.shape
    for i in range(row):
        for j in range(col):
            if grid[i, j] != None:
                neighbors = []
                # 1
                if i - 1 >= 0 and j - 1 >= 0:
                    if grid[i - 1, j - 1] != None:
                        neighbors.append(grid[i - 1, j - 1])
                # 2
                if i - 1 >= 0:
                    if grid[i - 1, j] != None:
                        neighbors.append(grid[i - 1, j])
                # 3
                if i - 1 >= 0 and j + 1 <= GRID_SIZE - 1:
                    if grid[i - 1, j + 1] != None:
                        neighbors.append(grid[i - 1, j + 1])
                # 4
                if j - 1 >= 0:
                    if grid[i, j - 1] != None:
                        neighbors.append(grid[i, j - 1])
                # 5
                if j + 1 <= GRID_SIZE - 1:
                    if grid[i, j + 1] != None:
                        neighbors.append(grid[i, j + 1])
                # 6
                if i + 1 <= GRID_SIZE - 1 and j - 1 >= 0:
                    if grid[i + 1, j - 1] != None:
                        neighbors.append(grid[i + 1, j - 1])
                # 7
                if i + 1 <= GRID_SIZE - 1:
                    if grid[i + 1, j] != None:
                        neighbors.append(grid[i + 1, j])
                # 8
                if i + 1 <= GRID_SIZE - 1 and j + 1 <= GRID_SIZE - 1:
                    if grid[i + 1, j + 1] != None:
                        neighbors.append(grid[i + 1, j + 1])
                grid[i, j].neighbors = neighbors
    return grid, sum


def chooseRumourSpreaderSectionB(grid):
    rumour_spreader = grid[50, 50]
    return rumour_spreader


if __name__ == '__main__':
    main()
