from time import sleep

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap

grid_size = (10, 10)
arr = np.zeros(grid_size)
probToSetOnFire = 0.5

#init = np.random.rand(10, 10)
init = np.zeros((10,10))

fire_tree_pos = {}
tree_pos = {}
to_burn = {}

iteration = 0
matplotlib.use('TkAgg')

colors = ['green', '#654321', '#FF4500', 'black']
# colors = ['gray', 'blue', 'red']
cmap = ListedColormap(colors)

# fig = matplotlib.figure.Figure()
# myPlot = fig.imshow(init, cmap=cmap, vmin=0, vmax=2)
# plt.axis('off')
myPlot = None

# 0 - empty
# 1 - tree
# 2 - fire tree
# 3 - burned tree
def generate_trees(size, probabilities):
    return np.random.choice(np.arange(0, 4), p=probabilities, size=size)


def calculate_fire_spread_probability(grid, prob, burn_time):
    get_tree_pos_info(grid)
    global iteration
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
                    to_burn[cell_pos] = iteration
                    i = 1
                    break
    for item in to_burn:
        if iteration - to_burn[item] >= burn_time:
            grid[item] = 3
    iteration += 1
    return grid


def get_tree_pos_info(grid):
    global fire_tree_pos
    global tree_pos
    global to_burn

    tree_pos = {}
    fire_tree_pos = {}

    for row in range(len(grid)):
        for col in range(len(grid[1])):
            cell = grid[row, col]
            if cell == 2:
                fire_tree_pos[(row, col)] = cell
                to_burn[(row, col)] = iteration
            elif cell == 1:
                tree_pos[(row, col)] = cell


def update_plot(new_grid, canvas):
    myPlot.set_data(new_grid)
    # plt.draw()
    # plt.pause(1)
    canvas.draw()


def start_simulation(grid_size, probs):
    
    grid = generate_trees(grid_size, [1 - probs['density'] - probs['probability'], probs['density'], probs['probability']])
    return grid


def show_grid(grid):
    print(grid)


def set_plot(getplot):
    global myPlot
    myPlot = getplot 
    plt.axis('off')
    # return fig


# print(trees)
# plot_grid(trees)
# start_simulation(trees)
