import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from matplotlib.figure import Figure

grid_flag = False
sim_flag = False
grid_size = (0, 0)
sim_params = (0.0, 0.0)


def confirm_grid_size():
    gridx = entry1.get()
    gridy = entry2.get()
    print(f"X: {gridx}")
    print(f"Y: {gridy}")
    global grid_size
    grid_size = (int(gridx), int(gridy))

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
    print(f"Density: {density}")
    print(f"Probability: {probability}")
    global sim_params
    sim_params = (float(density), float(probability))
    
    global sim_flag
    sim_flag = True
    sim_button.config(state=tk.DISABLED)
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
    print('sim run')

def restet_pressed():
    global grid_flag
    global sim_flag
    global grid_size
    global sim_params

    grid_flag = False
    sim_flag = False
    grid_size = (0, 0)
    sim_params = (0.0, 0.0)

    grid_button.config(state=tk.NORMAL)
    sim_button.config(state=tk.NORMAL)
    run_button.config(state=tk.DISABLED)

# forest grid funcs

def create_grid(parent, rows, cols):
    global grid_entries
    grid_entries = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = tk.Entry(parent, width=2, justify='center')
            entry.grid(row=i, column=j, padx=2, pady=2)
            row_entries.append(entry)
        grid_entries.append(row_entries)

def read_element(row, col):
    try:
        return grid_entries[row][col].get()
    except IndexError:
        print(f"Invalid indices: ({row}, {col})")
        return None

def set_element(row, col, value):
    try:
        grid_entries[row][col].delete(0, tk.END)
        grid_entries[row][col].insert(0, value)
    except IndexError:
        print(f"Invalid indices: ({row}, {col})")

root = tk.Tk()
root.title("Forest Fire")

# Grid size
r = 0

vcmd = root.register(validate_input1)

label1 = tk.Label(root, text="X:")
label1.grid(row=r, column=0, padx=10, pady=0)

entry1 = tk.Entry(root, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry1.insert(0, '0')
entry1.grid(row=r, column=1, padx=10, pady=0)


grid_button = tk.Button(root, text="Confirm Grid Size", command=confirm_grid_size)
grid_button.grid(row=r, column=3, rowspan=2, pady=0)
r += 1


label2 = tk.Label(root, text="Y:")
label2.grid(row=r, column=0, padx=10, pady=0)

entry2 = tk.Entry(root, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry2.insert(0, '0')
entry2.grid(row=r, column=1, padx=10, pady=0)
r += 1
# Sim params

vcmd = root.register(validate_input2)

    # forest density
label3 = tk.Label(root, text="Density:")
label3.grid(row=r, column=0, padx=10, pady=0)

entry3 = tk.Entry(root, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry3.insert(0, '0')
entry3.grid(row=r, column=1, padx=10, pady=0)

sim_button = tk.Button(root, text="Confirm Sim Params", command=confirm_sim_params)
sim_button.grid(row=r, column=3, rowspan=2, pady=0)
r += 1

    # fire spread probability
label4 = tk.Label(root, text="Probability:")
label4.grid(row=r, column=0, padx=10, pady=0)

entry4 = tk.Entry(root, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry4.insert(0, '0')
entry4.grid(row=r, column=1, padx=10, pady=0)
r += 1

    # wind
label5 = tk.Label(root, text="Wind (x,y)")
label5.grid(row=r, column=0, padx=10, pady=0)

entry5x = tk.Entry(root, validate="key", validatecommand=(vcmd, '%d', '%P'), width=10)
entry5x.insert(0, '0')
entry5x.grid(row=r, column=1, padx=10, pady=0)

entry5x = tk.Entry(root, validate="key", validatecommand=(vcmd, '%d', '%P'), width=10)
entry5x.insert(0, '0')
entry5x.grid(row=r, column=10, padx=10, pady=0)
r += 1

# forest grid - matplotlib

fig = Figure(figsize = (5, 5), dpi = 100) 

canvas = FigureCanvasTkAgg(fig, master = root)   
canvas.draw()
# placing the canvas on the Tkinter window 
canvas.get_tk_widget().grid(row=r, column=0, columnspan=4)
r += 1

# run

reset_button = tk.Button(root, text="Reset", command=restet_pressed)
reset_button.grid(row=6, column=0, columnspan=1, pady=20)

run_button = tk.Button(root, text="Start", command=run_pressed, state=tk.DISABLED)
run_button.grid(row=6, column=1, columnspan=1, pady=20)

root.mainloop()
