import math

# Step 1: Ask the user for a number
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
if num < 0:
    print("Square root and logarithm are not defined for negative numbers.")
else:
    square_root = math.sqrt(num)
    natural_log = math.log(num)

    # Step 3: Display results
    print("Square root of", num, "is:", square_root)
    print("Natural logarithm (ln) of", num, "is:", natural_log)

# Sine can be calculated for any real number
sine_value = math.sin(num)
print("Sine of", num, "radians is:", sine_value)
