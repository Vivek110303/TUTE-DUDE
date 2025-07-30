# task1_read_file.py

def read_file():
    try:
        with open("sample.txt", "r") as file:
            print("File content:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: 'sample.txt' does not exist.")

# Run the function
read_file()
