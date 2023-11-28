import sys

import numpy as np
import pygame
from matplotlib import pyplot as plt

from displays.input import Input
from displays.label import Label
from level import Type

pygame.init()
size = (width, height) = 750, 550
screen = pygame.display.set_mode(size) # resolution of screen
pygame.display.set_caption('Rumour Spreading as Game Life') # title
clock = pygame.time.Clock()


def Settings(p, l, levels_probs, iterations):
    # create an instance
    label_p = Label(20, 50, "Population density:")
    label_l = Label(20, 100, "Generations to wait until spreading the rumour again:")
    label_levels_probs = Label(20, 150, "Probability for each skepticism")
    label_levels_probs_1 = Label(380, 150, "S1")
    label_levels_probs_2 = Label(380, 200, "S2")
    label_levels_probs_3 = Label(380, 250, "S3")
    label_levels_probs_4 = Label(380, 300, "S4")
    label_iterations = Label(20, 350, "Maximum number of iterations:")
    label_pause = Label(20, 450, "To pause the animation press space.")
    label_start = Label(20, 500, "To start the animation press Enter.")
    input_p = Input(420, 40, 50, 32, str(p))
    input_l = Input(600, 90, 50, 32, str(l))
    input_levels_probs_1 = Input(420, 140, 50, 32, str(levels_probs[1]))
    input_levels_probs_2 = Input(420, 190, 50, 32, str(levels_probs[2]))
    input_levels_probs_3 = Input(420, 240, 50, 32, str(levels_probs[3]))
    input_levels_probs_4 = Input(420, 290, 50, 32, str(levels_probs[4]))
    input_iterations = Input(420, 340, 50, 32, str(iterations))
    labels = [label_p, label_l, label_levels_probs, label_levels_probs_1,
              label_levels_probs_2, label_levels_probs_3, label_levels_probs_4,
              label_iterations, label_pause, label_start]
    input_boxes = [input_p, input_l, input_levels_probs_1, input_levels_probs_2,
                   input_levels_probs_3, input_levels_probs_4, input_iterations]
    done = False    # when user finish update the params
    # start the settings loop
    while not done:
        # handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # exit - X
                pygame.quit()
                quit()
            for box in input_boxes:
                box.handle_event(event)     # handle inputs changes
            if event.type == pygame.KEYDOWN:        # at the end press Enter
                if event.key == pygame.K_RETURN:
                    p = float(input_p.text)
                    l = int(input_l.text)
                    levels_probs[1] = float(input_levels_probs_1.text)
                    levels_probs[2] = float(input_levels_probs_2.text)
                    levels_probs[3] = float(input_levels_probs_3.text)
                    levels_probs[4] = float(input_levels_probs_4.text)
                    iterations = int(input_iterations.text)
                    done = True
        # update the inputs
        for box in input_boxes:
            box.update()
        # draw the screen from begin
        screen.fill((102,178,255))
        # draw the input sprite on the screen
        for box in input_boxes:
            box.draw(screen)
        for box in labels:
            box.draw(screen)
        # update the display
        pygame.display.update()
        clock.tick(30)
    return p, l, levels_probs, iterations

def gameLoop(iterations, grid, iterationFunc, people_sum):
    current_iter = 0
    believers_sum = 1
    believers_percent = []
    while current_iter < iterations and believers_sum != 0:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # If it's a QUIT event, the game is closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:        # if it's a SPACE keydown event, the game is paused
                if event.key == pygame.K_SPACE:
                    pause()
        # logic
        rows, cols = grid.shape
        block_width = float(screen.get_width() / cols)
        block_height = float(screen.get_height() / rows)
        believers_sum = 0
        line_color = (224, 224, 224)
        screen.fill(line_color)
        for i in range(cols):
            for j in range(rows):
                x = i * block_width
                y = j * block_height
                cell = grid[i][j]
                if cell is not None:
                    if cell.isBeliever:   # draw believers
                        pygame.draw.rect(screen, (255, 0, 0), (x, y, block_width, block_height))
                        believers_sum += 1
                    else:   # draw non believers
                        pygame.draw.rect(screen, (0, 0, 0), (x, y, block_width, block_height))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, block_width, block_height))
                pygame.draw.line(screen, line_color, (x, y), (x, screen.get_height()))
                pygame.draw.line(screen, line_color, (x, y), (screen.get_width(), y))
        believers_percent.append((believers_sum / people_sum) * 100)
        pygame.display.update()
        clock.tick(30)
        # iterate once
        new_grid = iterationFunc(grid)
        grid = new_grid
        current_iter += 1
    show_graph(current_iter, believers_percent)


def pause():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


def show_graph(iterations, believers_percent):
    iteration = np.arange(1, iterations + 1)
    believers = np.array(believers_percent)
    plt.plot(iteration, believers)
    plt.ylabel('Believers percent')
    plt.xlabel('Iteration')
    plt.show()


'''
Section B functions
'''

def gameLoopSectionB(iterations, grid, iterationFunc, people_sum):
    current_iter = 0
    believers_sum = 1
    believers_percent = []
    while current_iter < iterations and believers_sum != 0:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # If it's a QUIT event, the game is closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:        # if it's a SPACE keydown event, the game is paused
                if event.key == pygame.K_SPACE:
                    pause()
        # logic
        rows, cols = grid.shape
        block_width = float(screen.get_width() / cols)
        block_height = float(screen.get_height() / rows)
        believers_sum = 0
        line_color = (224, 224, 224)
        screen.fill(line_color)
        for i in range(cols):
            for j in range(rows):
                x = i * block_width
                y = j * block_height
                cell = grid[i][j]
                if cell is not None:
                    if cell.isBeliever:   # draw believers
                        pygame.draw.rect(screen, (255, 0, 0), (x, y, block_width, block_height))
                        believers_sum += 1
                    else:   # draw non believers
                        if cell.level.type == Type.S1:
                            pygame.draw.rect(screen, (255, 255, 0), (x, y, block_width, block_height))
                        elif cell.level.type == Type.S2:
                            pygame.draw.rect(screen, (51, 51, 255), (x, y, block_width, block_height))
                        elif cell.level.type == Type.S3:
                            pygame.draw.rect(screen, (255, 0, 255), (x, y, block_width, block_height))
                        elif cell.level.type == Type.S4:
                            pygame.draw.rect(screen, (51, 255, 51), (x, y, block_width, block_height))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, block_width, block_height))
                pygame.draw.line(screen, line_color, (x, y), (x, screen.get_height()))
                pygame.draw.line(screen, line_color, (x, y), (screen.get_width(), y))
        believers_percent.append((believers_sum / people_sum) * 100)
        pygame.display.update()
        # clock.tick(2)
        clock.tick(30)
        # iterate once
        new_grid = iterationFunc(grid)
        grid = new_grid
        current_iter += 1
    show_graph(current_iter, believers_percent)

