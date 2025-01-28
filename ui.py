import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)  # type: ignore
from matplotlib.figure import Figure # type: ignore

import numpy as np
from matplotlib.colors import ListedColormap

import time

import sim

run_flag  = False

def confirm_grid_size():
    entry1.config(state=tk.DISABLED)
    entry7.config(state=tk.DISABLED)
    entry8.config(state=tk.DISABLED)

    burn_rate = entry7.get()
    starting_no = entry8.get()
    global numerical
    numerical = {
        'burn': float(burn_rate),
        'starting': float(starting_no)
        }

    gridx = entry1.get()
    # gridy = entry2.get()
    print(f"LxL: {gridx}x{gridx}")
    print(f"Starting fires: {starting_no}")
    print(f'Burn rate: {burn_rate}')
    # print(f"Y: {gridy}")
    global grid_size
    grid_size = (int(gridx), int(gridx))

    im_data = np.random.random(grid_size)
    im_plt = ax.imshow(im_data, cmap=cmap, vmin=0, vmax=3)
    sim.set_plot(im_plt)

    global grid_flag
    grid_flag = True
    grid_button.config(state=tk.DISABLED)
    check_buttons()


def validate_input1(action, value_if_allowed):
    if action == '1':  # '1' indicates an insert action
        return value_if_allowed.isdigit()
    return True


def confirm_sim_params():
    density = entry3.get()
    probability = entry4.get()
    wind = (entry5x.get(), entry5y.get())
    growth_chance = entry6.get()
    burn_rate = entry7.get()
    print(f"Density: {density}")
    print(f"Probability: {probability}")
    print(f'Wind: ({wind[0]}, {wind[1]})')
    print(f'Growth chance: {growth_chance}')
    global sim_params
    sim_params = {
        'density': float(density),
        'probability': float(probability),
        'wind': tuple(map(float, wind)),
        'growth': float(growth_chance),
        'burn': float(burn_rate)
        }

    global sim_flag
    sim_flag = True
    sim_button.config(state=tk.DISABLED)

    entry3.config(state=tk.DISABLED)
    entry4.config(state=tk.DISABLED)
    entry5x.config(state=tk.DISABLED)
    entry5y.config(state=tk.DISABLED)
    entry6.config(state=tk.DISABLED)

    check_buttons()


def validate_input2(action, value_if_allowed):
    if action == '1':  # '1' indicates an insert action
        try:
            value = float(value_if_allowed)
            return 0.0 <= value <= 1.0
        except ValueError:
            return False
    return True


def check_buttons():
    print(grid_flag, sim_flag)
    if grid_flag and sim_flag:
        run_button.config(state=tk.NORMAL)


def run_pressed():
    run_button.config(state=tk.DISABLED)
    sp = sim_params | numerical
    print('sim run')
    global grid
    grid = sim.start_simulation(grid_size, sp)
    global run_flag
    run_flag = True



def restet_pressed():
    global grid_flag
    global sim_flag
    global grid_size
    global sim_params
    global run_flag
    
    run_flag = False
    grid_flag = False
    sim_flag = False
    grid_size = (0, 0)
    sim_params = (0.0, 0.0)

    grid_button.config(state=tk.NORMAL)
    sim_button.config(state=tk.NORMAL)
    run_button.config(state=tk.DISABLED)

    entry1.config(state=tk.NORMAL)
    entry3.config(state=tk.NORMAL)
    entry4.config(state=tk.NORMAL)
    entry5x.config(state=tk.NORMAL)
    entry5y.config(state=tk.NORMAL)
    entry6.config(state=tk.NORMAL)
    entry7.config(state=tk.NORMAL)
    entry8.config(state=tk.NORMAL)


grid_flag = False
sim_flag = False
grid_size = (0, 0)
sim_params = (0.0, 0.0)

root = tk.Tk()
root.title("Forest Fire")


# Frames up
frame_up = tk.Frame(root)
frame_up.pack(pady=10)

frame_up_L = tk.Frame(frame_up)
frame_up_C = tk.Frame(frame_up)
frame_up_R = tk.Frame(frame_up)
frame_up_L.pack(side='left')
frame_up_C.pack(side='left')
frame_up_R.pack(side='left')

# XY input
vcmdn = root.register(validate_input1)

label1 = tk.Label(frame_up_L, text="L:")
label1.pack()
entry1 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmdn, '%d', '%P'))
entry1.insert(0, '45')
entry1.pack()

grid_button = tk.Button(frame_up_R, text="Confirm Numerical", command=confirm_grid_size)
grid_button.pack()

label7 = tk.Label(frame_up_L, text="Burn Rate:")
label7.pack()
entry7 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmdn, '%d', '%P'))
entry7.insert(0, '4')
entry7.pack()

label8 = tk.Label(frame_up_L, text="Starting Fires:")
label8.pack()
entry8 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmdn, '%d', '%P'))
entry8.insert(0, '1')
entry8.pack()

# forest density
 
vcmd = root.register(validate_input2)

label3 = tk.Label(frame_up_L, text="Density:")
label3.pack()
entry3 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry3.insert(0, '0.4')
entry3.pack()

label4 = tk.Label(frame_up_L, text="Spread Probability:")
label4.pack()
entry4 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry4.insert(0, '0.1')
entry4.pack()

label6 = tk.Label(frame_up_L, text="Growth chance:")
label6.pack()
entry6 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry6.insert(0, '0.1')
entry6.pack()

label5 = tk.Label(frame_up_L, text="Wind (x,y)")
label5.pack()
frame_up_C_wind = tk.Frame(frame_up_C)
frame_up_C_wind.pack()
entry5x = tk.Entry(frame_up_C_wind, validate="key",
                    validatecommand=(vcmd, '%d', '%P'), width=10)
entry5x.insert(0, '0')
entry5x.pack(side='left')
entry5y = tk.Entry(frame_up_C_wind, validate="key",
                    validatecommand=(vcmd, '%d', '%P'), width=10)
entry5y.insert(0, '0')
entry5y.pack(side='left')

spacer = tk.Label(frame_up_R, text="\n\n")
spacer.pack()

sim_button = tk.Button(frame_up_R, text="Confirm Sim Params", command=confirm_sim_params)
sim_button.pack()

# forest grid - matplotlib
frame_plot = tk.Frame(root)
frame_plot.pack(pady=10)


colors = ['green', '#654321', '#FF4500', 'black']
# colors = ['gray', 'blue', 'red']
cmap = ListedColormap(colors)


fig = Figure(figsize = (5, 5), dpi = 100)
ax = fig.add_subplot(111)
ax.axis('off')
im_data = np.random.random((10,10))
im_plt = ax.imshow(im_data, cmap=cmap, vmin=0, vmax=3)

sim.set_plot(im_plt)

canvas = FigureCanvasTkAgg(fig, master = frame_plot)
# placing the canvas on the Tkinter window 
canvas.get_tk_widget().pack()


# run

frame_bottom = tk.Frame(root)
frame_bottom.pack()

reset_button = tk.Button(frame_bottom, text="Reset", command=restet_pressed)
reset_button.pack(side='left')

run_button = tk.Button(frame_bottom, text="Start", command=run_pressed, state=tk.DISABLED)
run_button.pack(side='left')

tp = time.time()
while True:
    root.update()
    # print(time.time() - tp)
    if run_flag and (time.time() - tp) > 0.4:
        grid = sim.calculate_fire_spread_probability(grid, 0.95, sim_params['burn'], sim_params['growth'], sim_params['wind'])
        print(grid)
        sim.update_plot(grid, canvas)
        tp = time.time()