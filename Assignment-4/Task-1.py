try:
    with open("sample.txt", "r") as file:
        line_number = 1
        for line in file:
            print(f"line {line_number}:{line.strip()}")
            line_number += 1
except FileNotFoundError:
    print("the file sample not found")
