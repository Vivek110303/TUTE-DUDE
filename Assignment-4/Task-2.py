# task2_write_append_file.py

def write_and_append():
    # Step 1: Write user input to file
    user_input = input("Enter some data to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")

    # Step 2: Append more data
    more_input = input("Enter additional data to append: ")
    with open("output.txt", "a") as file:
        file.write(more_input + "\n")

    # Step 3: Read and display final content
    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        print(file.read())

# Run the function
write_and_append()
