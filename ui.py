import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)  # type: ignore
from matplotlib.figure import Figure # type: ignore

from funs import (confirm_grid_size, validate_input1, confirm_sim_params, validate_input2, check_buttons, run_pressed, restet_pressed)

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
vcmd = root.register(validate_input1)

label1 = tk.Label(frame_up_L, text="X:")
label1.pack()
entry1 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry1.insert(0, '0')
entry1.pack()

label2 = tk.Label(frame_up_L, text="Y:")
label2.pack()
entry2 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry2.insert(0, '0')
entry2.pack()

grid_button = tk.Button(frame_up_R, text="Confirm Grid Size", command=confirm_grid_size)
grid_button.pack()

# forest density
 
vcmd = root.register(validate_input2)

label3 = tk.Label(frame_up_L, text="Density:")
label3.pack()
entry3 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry3.insert(0, '0')
entry3.pack()

label4 = tk.Label(frame_up_L, text="Probability:")
label4.pack()
entry4 = tk.Entry(frame_up_C, validate="key", validatecommand=(vcmd, '%d', '%P'))
entry4.insert(0, '0')
entry4.pack()

label5 = tk.Label(frame_up_L, text="Wind (x,y)")
label5.pack()
frame_up_C_wind = tk.Frame(frame_up_C)
frame_up_C_wind.pack()
entry5x = tk.Entry(frame_up_C_wind, validate="key", validatecommand=(vcmd, '%d', '%P'), width=10)
entry5x.insert(0, '0')
entry5x.pack(side='left')
entry5y = tk.Entry(frame_up_C_wind, validate="key", validatecommand=(vcmd, '%d', '%P'), width=10)
entry5y.insert(0, '0')
entry5y.pack(side='left')

sim_button = tk.Button(frame_up_R, text="Confirm Sim Params", command=confirm_sim_params)
sim_button.pack()

# forest grid - matplotlib
frame_plot = tk.Frame(root)
frame_plot.pack(pady=10)

fig = Figure(figsize = (5, 5), dpi = 100) 

canvas = FigureCanvasTkAgg(fig, master = frame_plot)   
canvas.draw()
# placing the canvas on the Tkinter window 
canvas.get_tk_widget().pack()

# run

frame_bottom = tk.Frame(root)
frame_bottom.pack()

reset_button = tk.Button(frame_bottom, text="Reset", command=restet_pressed)
reset_button.pack(side='left')

run_button = tk.Button(frame_bottom, text="Start", command=run_pressed, state=tk.DISABLED)
run_button.pack(side='left')

root.mainloop()
