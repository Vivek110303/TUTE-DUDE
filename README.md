

# Python Assignments – Complete Documentation  

This repository contains a collection of Python assignments that cover **basic to advanced programming concepts**, including **mathematics, conditionals, recursion, file handling, data structures, GUI programming (Tkinter), simple games, and automation using Selenium**.  

These assignments are designed as **step-by-step practical exercises** to build strong foundations in **Python programming** and provide exposure to **real-world applications** like **web automation and GUI applications**.  

***

## Assignment 1 – Basic Arithmetic and String Handling  

### Task 1: Arithmetic Operations  
A simple program that takes two numbers and performs:  
- Addition  
- Subtraction  
- Multiplication  
- Division  

 Concepts Used:  
- `input()` for user input  
- Arithmetic operators (`+`, `-`, `*`, `/`)  
- `print()` formatting  

***

### Task 2: Greeting with Full Name  
The program asks for **first name and last name**, concatenates them, and prints a **personalized message**.  

 Concepts Used:  
- String concatenation (`+`)  
- User input and output formatting  

***

##  Assignment 2 – Conditionals and Loops  

### Task 1: Odd or Even Check  
Checks if a given number is **even or odd** using the modulus `%` operator.  

### Task 2: Summation using Loops  
Calculates the **sum of numbers from 1 to 50** using a `for` loop.  

 Concepts Used:  
- Conditional statements (`if-else`)  
- Loops (`for`)  
- Cumulative summation  

***

##  Assignment 3 – Recursion and Math Module  

### Task 1: Factorial with Recursion  
Takes a number as input and calculates factorial using a **recursive function**.  

- Handles **negative numbers gracefully** by giving an error message.  

### Task 2: Using Python’s `math` module  
Performs multiple calculations:  
- Square root  
- Natural Logarithm (`ln`)  
- Sine (in radians)  

 Concepts Used:  
- Recursive functions  
- Importing and using the `math` module  

***

##  Assignment 4 – File Handling  

### Task 1: Read a File  
Reads **contents of a text file (`sample.txt`)** and displays it line by line.  

### Task 2: Write and Append to a File  
- Writes user input into `output.txt`  
- Appends more data  
- Reads back and displays the final file content  

 Concepts Used:  
- File operations (`read`, `write`, `append`)  
- Exception handling (`try-except`)  

***

##  Assignment 5 – Data Structures  

### Task 1: Dictionary  
- Stores student names and marks in a dictionary  
- Retrieves marks based on **user input**  

### Task 2: List Operations  
- Creates a list of numbers from 1–10  
- Extracts the first five elements  
- Reverses the extracted portion  

 Concepts Used:  
- Dictionaries (key-value pairs)  
- Lists and list slicing  
- Reversing lists  

***

##  Assignment 6 – GUI Calculator (Tkinter)  

A **simple calculator application** built using **Tkinter**, Python’s standard GUI toolkit.  

✨ Features:  
- Supports **Addition, Subtraction, Multiplication, Division**  
- Includes **Clear** and **Equal** buttons  
- Error handling for division by zero  

 Concepts Used:  
- Tkinter `Button`, `Entry`, `Label`, `place()` for positioning  
- Event handling with `command` functions  
- Global state management (`+`, `-`, `*`, `/`)  

***

##  Assignment 7 – Rock Paper Scissors Game  

A console-based **Rock Paper Scissors** game where:  
- The player competes against the **computer**  
- Random moves chosen using `random.choice()`  
- Validates invalid inputs  
- Determines winner (Player/Computer/Tie)  

 Concepts Used:  
- Loops and conditionals  
- Random number generation  
- Game logic implementation  

***

##  Assignment 8 – Selenium Automation  

### Task 1: Automating Facebook Login and Status Post *(Demo Credentials Used)*  
Steps performed:  
1. Opens Facebook login page  
2. Enters email & password  
3. Clicks login button  
4. Posts a status message  

 Concepts Used:  
- Selenium WebDriver (Firefox)  
- Locating elements by **ID, NAME, TAG_NAME**  
- Explicit waits (`WebDriverWait`)  
- Exception handling  


***

### Task 2: Amazon Product Search  
- Opens **Amazon.in**  
- Searches for "iPhones"  
- Displays number of results found  
- Prints product names  

 Concepts Used:  
- Selenium WebDriver (Chrome)  
- Locating elements with **XPath**  
- Iterating through results  

***

### Task 3: Google Automation  
- Opens Google in Chrome  
- Waits for 5 seconds  
- Refreshes page  
- Waits again before exiting  

 Concepts Used:  
- Selenium with Chrome WebDriver  
- Browser navigation commands (`get`, `refresh`, `quit`)  
- `time.sleep()` for delays  

***

# � Technologies & Concepts Covered  

- **Core Python:** Variables, Operators, Conditionals, Loops  
- **Functions:** Recursive functions  
- **Math:** Using Python’s `math` library  
- **File Handling:** Reading, Writing, Appending files  
- **Data Structures:** Lists, Dictionaries, String manipulation  
- **Exception Handling:** Try/Except blocks  
- **GUI Applications:** Tkinter for creating a calculator  
- **Game Development:** Console-based Rock Paper Scissors  
- **Web Automation:** Selenium with Chrome & Firefox drivers  

***

#  How to Run  

1. Install **Python 3.x** on your system  
2. Clone this repository or copy the assignment files  
3. Run any script with:  

```bash
python filename.py
```

4. For Selenium Assignments:  
   - Install Selenium → `pip install selenium`  
   - Download the latest **ChromeDriver/GeckoDriver** and keep it in PATH  

***

#  Conclusion  

These assignments progressively cover **basic programming** to **real-world automation tasks**. By completing them, one gains:  
- Strong foundation in **Python basics**  
- Practical knowledge of **file handling & data structures**  
- Exposure to **GUI development** with Tkinter  
- Experience with **automation and web scraping using Selenium**  
