# ==================================================
# Loops Assignment - for and while practice
# ==================================================


# --------------------------------------------------
# Problem 1: Sum of integers in a range
# --------------------------------------------------
# Description:
# Calculates the sum of all integers from 1 to n and
# the sum of only even numbers in that range using a for loop.
#
# Inputs:
# - n (int)
#
# Outputs:
# - Sum 1..n
# - Even sum 1..n
#
# Validations:
# - n must be an integer >= 1
#
# Test cases:
# 1) Normal: n = 10
# 2) Edge case: n = 1
# 3) Error: n = -5

try:
    n = int(input("Enter n: "))
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Multiplication table with for
# --------------------------------------------------
# Description:
# Displays the multiplication table of a number from 1 to m.
#
# Inputs:
# - base (int)
# - m (int)
#
# Outputs:
# - Multiplication table lines
#
# Validations:
# - m >= 1
#
# Test cases:
# 1) Normal: base=5, m=4
# 2) Edge case: base=3, m=1
# 3) Error: m=0

try:
    base = int(input("Enter base number: "))
    m = int(input("Enter limit: "))

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# --------------------------------------------------
# Description:
# Reads numbers until a sentinel value is entered and
# calculates the average of valid numbers.
#
# Inputs:
# - number (float)
#
# Outputs:
# - Count
# - Average
#
# Validations:
# - Only numbers >= 0 are accepted
#
# Test cases:
# 1) Normal: 10, 20, 30, -1
# 2) Edge case: -1
# 3) Error: text input

SENTINEL_VALUE = -1
count = 0
total = 0.0

while True:
    user_input = input("Enter a number (-1 to finish): ")

    try:
        number = float(user_input)
    except ValueError:
        print("Error: invalid input")
        continue

    if number == SENTINEL_VALUE:
        break

    if number < 0:
        print("Error: invalid input")
        continue

    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)


# --------------------------------------------------
# Problem 4: Password attempts with while
# --------------------------------------------------
# Description:
# Simulates a password login system with limited attempts.
#
# Inputs:
# - user_password (string)
#
# Outputs:
# - Login success or Account locked
#
# Validations:
# - Limited attempts
#
# Test cases:
# 1) Normal: correct password on first try
# 2) Edge case: correct password on last try
# 3) Error: all wrong attempts

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break

    attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")


# --------------------------------------------------
# Problem 5: Simple menu with while
# --------------------------------------------------
# Description:
# Displays a menu that runs until the user chooses to exit.
#
# Inputs:
# - option (int)
#
# Outputs:
# - Menu actions
#
# Validations:
# - Option must be valid
#
# Test cases:
# 1) Normal: options 1,2,3,0
# 2) Edge case: option 0
# 3) Error: invalid option

counter = 0
option = -1

while option != 0:
    print("\nMenu")
    print("1) Show greeting")
    print("2) Show counter")
    print("3) Increment counter")
    print("0) Exit")

    user_input = input("Choose an option: ")

    try:
        option = int(user_input)
    except ValueError:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
    else:
        print("Error: invalid option")


# --------------------------------------------------
# Problem 6: Pattern printing with nested loops
# --------------------------------------------------
# Description:
# Prints a right triangle pattern using nested for loops.
#
# Inputs:
# - n (int)
#
# Outputs:
# - Triangle pattern
#
# Validations:
# - n >= 1
#
# Test cases:
# 1) Normal: n=4
# 2) Edge case: n=1
# 3) Error: n=0

try:
    n = int(input("Enter number of rows: "))

    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)
except ValueError:
    print("Error: invalid input")
