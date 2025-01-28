from time import sleep

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap

grid_size = (10, 10)
arr = np.zeros(grid_size)
probToSetOnFire = 0.5

# init = np.random.rand(10, 10)
init = np.zeros((10, 10))

fire_tree_pos = {}
tree_pos = {}
grass_pos = {}
to_burn = {}

iteration = 0
matplotlib.use('TkAgg')

# colors = ['green', '#654321', '#FF4500', 'gray']
# colors = ['gray', 'blue', 'red']
# cmap = ListedColormap(colors)

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


def calculate_fire_spread_probability(grid, prob, burn_rate, growth_chance, wind):
    get_tree_pos_info(grid, burn_rate)
    global iteration
    for cell_pos in tree_pos:
        row = cell_pos[0]
        col = cell_pos[1]

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):

                sel_pos = (row + i, col + j)

                if sel_pos not in fire_tree_pos:
                    continue
                probability = np.random.random()

                match (i, j):
                    case (-1, -1) | (-1, 1) | (1, -1) | (1, 1):
                        probability += (j*wind[0] + i*wind[1]) / 2
                    case (-1, 0) | (1, 0):
                        probability += i*wind[1]
                    case (0, -1) | (0, 1):
                        probability += j*wind[0]

                if probability >= prob:
                    grid[cell_pos] = 2
                    to_burn[cell_pos] = iteration + burn_rate
                    break

    for item in to_burn:
        if iteration == to_burn[item]:
            grid[item] = 3
            to_burn[item] = -1 * (iteration + 1)
        elif -1 * iteration == to_burn[item]:
            if np.random.random() <= growth_chance:
                grid[item] = 1
                to_burn[item] = -1
            else:
                to_burn[item] = -1 * (iteration + 1)

    for item in grass_pos:
        if np.random.random() <= growth_chance:
            grid[item] = 1
            grass_pos[item] = item

    iteration += 1
    return grid


def get_tree_pos_info(grid, burn_rate):
    global grass_pos
    global fire_tree_pos
    global tree_pos
    global to_burn

    tree_pos = {}
    grass_pos = {}
    fire_tree_pos = {}

    for row in range(len(grid)):
        for col in range(len(grid[1])):
            cell = grid[row, col]
            if cell == 2:
                fire_tree_pos[(row, col)] = cell
                if (row, col) not in to_burn:
                    to_burn[(row, col)] = iteration + burn_rate
            elif cell == 1:
                tree_pos[(row, col)] = cell
            elif cell == 0:
                grass_pos[(row, col)] = cell


def update_plot(new_grid, canvas):
    myPlot.set_data(new_grid)
    # plt.draw()
    # plt.pause(1)
    canvas.draw()


def start_simulation(grid_size, probs):
    grid = generate_trees(grid_size,
                          [1 - probs['density'] - probs['starting'], probs['density'], probs['starting'], 0])
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
