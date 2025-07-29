
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("\nData successfully written to output.txt.")


additional_text = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_text + "\n")
print("\nData successfully appended.")


print("\nFinal content of output.txt:\n")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
