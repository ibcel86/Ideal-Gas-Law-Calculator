# Ideal Gas Law Calculator
A Python script using tkinter GUI for a simple gas law calculator

The tkinter GUI has user inputs for pressure, temperature, volume and moles. The user inputs the values they wish to use and selects the units from a dropdown.

**How The Script Works**

The python script is provided and is documented to show how each function works. A quick overview:

The formula for the ideal gas equation is pv=nRT. The user can input values to work out pressure, or the user can input values to calculate volume, or the number of 
moles, or the temperature. The calculate function has an error check that ensures the user must leave an entry blank. For example, if the user leave pressure blank, the code is written such that if p=None, then calculate p = nRT/V. If the user fills in all entries, the error check in the function displays "Leave one entry blank" on the GUI to remind the user that they need to leave an entry blank to use the calculator. 

The unit combinations are also checked: only valid unit selections are allowed and the function also checks that the selections are valid. The calculation requires the correct gas constant, r, which is provided in a dictionary that the function checks. If the unit combination is in the dictionary, the function calls the value from that key and uses it in the calculation. Where the unit combination does not exist, the user is reminded to select a valid combination.

The program also ensures units are selected for pressure, and volume so that the correct unit is displayed for the calculation. For example, if the user leaves pressure blank, the code will know to calculate pressure, but if the user does not select the unit for pressure this throws and error and the user is reminded to select the unit they want pressure to be calculted in. 

Once all of the conditions are satisfied, the calculate function executes and the result is displayed in the UI.

The UI has three buttons: quit, calculate, and clear. The quit button runs the tkinter function that closes the window. The calculate button executes the calculate function, and the Clear button executes the clear function so all user inputs are empty and all user unit selections are empty.

The calculator only uses metric units and is not coded for imperial units. This is because in science, we use SI units and not imperial units; though the dictionary can be updated with imperial unit combinations with the associated r values. Due to the large number of unit combinations and associated r values, if more unit combinations and r values were to be included in the calculator, the dictionary could be removed and a csv file containing the unit combinations and r values could be used instead. To hard code a dictionary with all of the associated keys and values would dwarf the lines of code, making readability difficult.
