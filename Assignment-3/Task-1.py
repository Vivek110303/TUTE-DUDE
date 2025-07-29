def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Take input from the user
num = int(input("Enter a number to find its factorial: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("Factorial of", num, "is:", result)
