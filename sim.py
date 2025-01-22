from time import sleep

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap

grid_size = (10, 10)
arr = np.zeros(grid_size)
probToSetOnFire = 0.5

init = np.random.rand(10, 10)

fire_tree_pos = {}
tree_pos = {}

matplotlib.use('TkAgg')

colors = ['green', '#654321', '#FF4500']
# colors = ['gray', 'blue', 'red']
cmap = ListedColormap(colors)

fig, ax = plt.subplots()
myPlot = ax.imshow(init, cmap=cmap, vmin=0, vmax=2)
plt.axis('off')


# 0 - empty
# 1 - tree
# 2 - fire tree
def generate_trees(size, probabilities):
    return np.random.choice(np.arange(0, 3), p=probabilities, size=size)


def calculate_fire_spread_probability(grid, prob):
    get_tree_pos_info(grid)

    for cell_pos in tree_pos:
        row = cell_pos[0]
        col = cell_pos[1]

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):

                sel_pos = (row + i, col + j)

                if sel_pos not in fire_tree_pos:
                    continue

                if np.random.random() >= prob:
                    grid[cell_pos] = 2
                    i = 1
                    break
    return grid


def get_tree_pos_info(grid):
    global fire_tree_pos
    global tree_pos

    tree_pos = {}
    fire_tree_pos = {}

    for row in range(len(grid)):
        for col in range(len(grid[1])):
            cell = grid[row, col]
            if cell == 2:
                fire_tree_pos[(row, col)] = cell
            elif cell == 1:
                tree_pos[(row, col)] = cell


def update_plot(new_grid):
    myPlot.set_data(new_grid)
    plt.draw()
    plt.pause(1)


def start_simulation(grid):
    while 1:
        grid = calculate_fire_spread_probability(grid, 0)
        update_plot(grid)


def show_grid(grid):
    print(grid)


trees = generate_trees(grid_size, [0.5, 0.4, 0.10])
print(trees)
# plot_grid(trees)
start_simulation(trees)
