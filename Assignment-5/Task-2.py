# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_first_five = first_five[::-1]

# Step 4: Print both the extracted and reversed lists
print("original data: ", numbers)
print("First five elements:", first_five)
print("Reversed list:", reversed_first_five)
