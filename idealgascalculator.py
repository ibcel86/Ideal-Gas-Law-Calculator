from tkinter import *
from tkinter import ttk

# Set up main window
window = Tk()
window.geometry("480x360")
window.title("Ideal Gas Law Calculator")

# Quit button
quit_button = ttk.Button(window, text="Quit", command=window.destroy)
quit_button.grid(column=2, row=5)

# Calculate button
calculate_button = ttk.Button(window, text="Calculate", command="")
calculate_button.grid(column=1, row=5)

# Welcome text
instruction_label = ttk.Label(window, text="Welcome to the Ideal Gas Law Calculator. \n Select the units you wish to calculate", 
background="", font=("Arial", 10, "normal"))
instruction_label.grid(column=2, row=0)
# Label and entry for typing in value for pressure
pressure_label = ttk.Label(window, text="Pressure", background="", font=("Arial", 10, "bold"))
pressure_entry = ttk.Entry(window, width=10, text="Pressure", background="", font=("Arial", 10, "normal"))
pressure_label.grid(column=0, row=1)
pressure_entry.grid(column=1, row=1)

# Label and entry for typing in value for volume
volume_label = ttk.Label(window, text="Volume", background="", font=("Arial", 10, "bold"))
volume_entry = ttk.Entry(window, width=10, text="Volume", background="", font=("Arial", 10, "normal"))
volume_label.grid(column=0, row=2)
volume_entry.grid(column=1, row=2)

# Label and entry for typing in value for temperature
temperature_label = ttk.Label(window, text="Temperature", background="", font=("Arial", 10, "bold"))
temperature_entry = ttk.Entry(window, width=10, text="Temperature", background="", font=("Arial", 10, "normal"))
temperature_label.grid(column=0, row=3)
temperature_entry.grid(column=1, row=3)

# Label and entry for typing in value for moles
moles_label = ttk.Label(window, text="Moles", background="", font=("Arial", 10, "bold"))
moles_entry = ttk.Entry(window, width=10, text="Moles", background="", font=("Arial", 10, "normal"))
moles_label.grid(column=0, row=4)
moles_entry.grid(column=1, row=4)

# Setting individual vars to prevent linked combobox commands
pressure_var = StringVar()
volume_var = StringVar()
temperature_var = StringVar()
moles_var = StringVar()

# Select units for pressure
pressure_selection = ttk.Combobox(window, width=12, text="Select unit: ", textvariable=pressure_var)
pressure_selection['values'] = ("Pa",
                                "atm",
                                "bar",
                                "psi")
pressure_selection.grid(column=2, row=1)

# Select units for volume
volume_selection = ttk.Combobox(window, width=12, text="Select unit: ", textvariable=volume_var)
volume_selection['values'] = ("dm3",
                                "L",
                                "m3")

volume_selection.grid(column=2, row=2)

def calculate_from_inputs():
    """Calculates an output based on user selection. 
    First, the input values are retreived as floats. Code first checks
    that input is a float and converts to a float. 

    Units are then retrieved and a check for valid unit combinations is checked.
    Dictionary containing values for gas constant 'r' are checked and relevent unit picked.

    Then the calculation is done based on user inputs.

    Error checking: ensures user inputs are correct. Ensures unit combinations are valid.

    Finally, the result is displayed.
    """
    try:
        # retrieve input values
        p = pressure_entry.get()
        v = volume_entry.get()
        t = temperature_entry.get()
        n = moles_entry.get()

        # Convert to floats (if they exist)
        p = float(p) if p else None
        v = float(v) if v else None
        t = float(t) if t else None
        n = float(n) if n else None

        # retrieve unit selections
        p_unit = pressure_var.get()
        v_unit = volume_var.get()
        t_unit = temperature_var.get()

        # Select appropriate gas constant (r) based on units
        r_values = {
            ("Pa", "dm3"): 8.314,
            ("Pa", "m3"): 8.314,
            ("Pa", "L"): 8314.46,
            ("atm", "dm3"): 0.0000821,  
            ("atm", "m3"): 0.0000821,
            ("atm", "L"): 0.00821,
            ("bar", "dm3"): 0.00008314,
            ("bar", "m3"): 0.00008314,  
            ("bar", "L"): 0.08314,  
            ("psi", "dm3"): 0.001205,
            ("psi", "m3"): 0.001205,
            ("psi", "L"): 1.205,  
             }

        # Match the gas constant based on unit selection
        r = r_values.get((p_unit, v_unit), None)

        if r is None:
            result_label.config(text="Unsupported unit combination.")
            return

        # Determine which variable to calculate
        if p is None:
            p = (n * r * t) / v
            result = f"Pressure = {p:,.2f} {p_unit}"
        elif v is None:
            v = (n * r * t) / p
            result = f"Volume = {v:,.2f} {v_unit}"
        elif t is None:
            t = (p * v) / (n * r)
            result = f"Temperature = {t:,.2f} {t_unit}"
        elif n is None:
            n = (p * v) / (r * t)
            result = f"Moles = {n:,.2f} mol"
        else:
            result = "Leave one field empty for calculation."

    except ValueError:
        result = "Invalid input. Please enter numeric values."

    # Display's the result in the label
    result_label.config(text=result)

def clear_entries():
    """Deletes entries so that user can restart a calculation without needing
    to restart the program or manually change values."""
    pressure_entry.delete(0, END)
    volume_entry.delete(0, END)
    temperature_entry.delete(0, END)
    moles_entry.delete(0, END)

    pressure_var.set("")
    volume_var.set("")
    temperature_var.set("")
    moles_var.set("")

    result_label.config(text="")

# Buttons and results display layout paramenters
clear_button = ttk.Button(window, text="Clear", command=clear_entries)
clear_button.grid(column=0, row=5)
calculate_button.config(command=calculate_from_inputs)
result_label = ttk.Label(window, text="", background="", font=("Arial", 10, "bold"))
result_label.grid(column=1, row=6, columnspan=2)

window.mainloop()