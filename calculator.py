# --- Fundamental Calculator Program ---

# 1. Data Declaration and Variable Initialisation
first_number = 0.0
second_number = 0.0
operation_choice = ""
calculation_result = 0.0

valid_operations = ["+", "-", "*", "/"]


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("ERROR: Please enter a valid numerical value.")


def calculate_result(first_number, second_number, operation_choice):
    if operation_choice == "+":
        return first_number + second_number
    elif operation_choice == "-":
        return first_number - second_number
    elif operation_choice == "*":
        return first_number * second_number
    elif operation_choice == "/":
        if second_number == 0:
           return "ERROR: Mathematical exception - division by zero is undefined."
        else:
            return first_number / second_number


# 2. User Inputs
print("--- Fundamental Calculator Program ---")

first_number = get_number("Please enter the first numerical value: ")
second_number = get_number("Please enter the second numerical value: ")

operation_choice = input("Please choose one arithmetic operator (+, -, *, /): ")

while operation_choice not in valid_operations:
    print("ERROR: Operation aborted due to an invalid arithmetic selection.")
    operation_choice = input("Please choose one arithmetic operator (+, -, *, /): ")


# 3. Calculation Logic
calculation_result = calculate_result(
    first_number,
    second_number,
    operation_choice
)


# 4. Display Result
if isinstance(calculation_result, str):
    print(calculation_result)
else:
    print("The final calculated result is:", calculation_result)