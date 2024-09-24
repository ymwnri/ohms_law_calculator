# Program: Ohm's Law Calculator
# Features: Calculate Voltage, Current, Resistance
# Procedure:
# 1. Ask for input for calcluation: Voltage, Current, Resistance
# 2. Ask appropriate values for calculation
# 3. Use Ohm's Law formula to calculate the missing value
# 4. Handle division by zero error
# 5. Display the result

def calculate_voltage(current, resistance):
    """Calculate Voltage using Ohm's Law.

    Args:
        current (float): The current in Amperes.
        resistance (float): The resistance in Ohms.

    Returns:
        float: The voltage in Volts.
    """
    voltage = current * resistance
    return voltage

def calculate_current(voltage, resistance):
    """Calculate Current using Ohm's Law.

    Args:
        voltage (float): The voltage in Volts.
        resistance (float): The resistance in Ohms.

    Returns:
        float: The current in Amperes.
    """
    current = voltage / resistance
    return current

def calculate_resistance(voltage, current):
    """Calculate Resistance using Ohm's Law.

    Args:
        voltage (float): The voltage in Volts.
        current (float): The current in Amperes.

    Returns:
        float: The resistance in Ohms.
    """
    resistance = voltage / current
    return resistance

# Start of the program
print("Welcome to Ohm's Law Calculator")
print("Select Calculation Type: \n1. Voltage \n2. Current \n3. Resistance\n")
input_type = int(input("Enter the Calculation Type: "))

# Control flow based on the input type
if input_type == 1:
    current = float(input("Enter Current (A): "))
    resistance = float(input("Enter Resistance (Ω): "))
    voltage = calculate_voltage(current, resistance)
    print(f"The Voltage is {voltage} Volts")

elif input_type == 2:
    voltage = float(input("Enter Voltage (V): "))
    resistance = float(input("Enter Resistance (Ω): "))
    try:
        current = calculate_current(voltage, resistance)
        print(f"The Current is {current} Amperes")
    except ZeroDivisionError:
        print("Cannot divide by zero")

elif input_type == 3:
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))
    try:
        resistance = calculate_resistance(voltage, current)
        print(f"The Resistance is {resistance} Ohms")
    except ZeroDivisionError:
        print("Cannot divide by zero")
        
else:
    print("Invalid Calculation Type")







