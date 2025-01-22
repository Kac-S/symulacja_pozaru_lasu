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
    wind = (entry5x.get(), entry5y.get())
    print(f"Density: {density}")
    print(f"Probability: {probability}")
    print(f'Wind: ({wind[0]}, {wind[1]})')
    global sim_params
    sim_params = {'density': float(density), 'probability': float(probability), 'wind': tuple(map(float, wind))}

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
