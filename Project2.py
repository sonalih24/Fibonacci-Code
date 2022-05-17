# File: Project2.py
# Student: Sonali Hornick
# UT EID: ssh2643
# Course Name: CS303E
# 
# Date: 04/02/2022
# Description of Program: This program builds a utility that allows the user to generate a list of the first N Fibonacci numbers (the function above), find and display the ith Fibonacci number, generate a list of Fibonacci numbers up to and possibly including the positive integer N, and find a list of Fibonacci numbers that add up to a non-negative integer N (more on that below).

# Sets constants to be used in program.
ERRORVALUE = "ERROR: Illegal value entered."
ERRORCOMMAND = "ERROR: Illegal command. Try again."
ZERO = "0"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"

def greatestFibNum(fib,n):
    # Records the largest Fibonacci number.
    k = (fib[0])
    for num in fib:
        if num <= n:
            k = num
    return k   

def largestFibNumsTotallingN():
    # Return Fibonacci numbers that sum to N.
    n = int(input("You've asked for Fibonacci numbers that sum to N. What is N? "))
    # If n < 0, invalid input.
    if n<0:
        print("ERROR: Illegal value entered.")
        getInput()
    # If n == 0, return list with 0.
    elif n==0: 
        print([0])
        getInput()
    else:
        # Initialize our list of summands found so far.
        summands = []
        # Initialize our list of Fibonacci numbers found so far.
        fib = [0,1]
        # Initialize result.
        result = 0
        # Use the previous two values to generate and record the next value.
        while result <= n:
            result = fib[-1] + fib[-2]
            fib.append(result)
        # Use the previous two values and greatestFibNum(fib,num) to generate and record the next value.
        while n>0:
            k = greatestFibNum(fib,n)
            n = n-k
            summands.append(k)
        print(summands)
        getInput()
    
def fibNumCountLessOrEqualN():
    # Return how many Fibonacci numbers are less than or equal to N.
    n = int(input("You've asked how many Fibonacci numbers are less than or equal to N. What is N? "))
    # If n < 0, return 0.
    if n<0: 
        print (0)
        getInput()
    # If n == 0, return 1.
    elif n==0: 
        print(1)
        getInput()
    else:
        # Initialize our list of Fibonacci numbers found so far.
        fib = [0,1]
        # Initialize result.
        result = 0
        while result <= n:
            # Use the previous two values to generate and record the next value.
            result = fib[-1] + fib[-2]
            # Add the newest value to the list we're creating.
            fib.append(result)
        print(len(fib)-1)
        getInput()

def fibNumbersLessOrEqualN():
    # Return the Fibonacci numbers less than or equal to N.
    n = int(input("You've asked for the Fibonacci numbers less than or equal to N. What is N? "))
    # If n < 0, return empty list.
    if n<0: 
        print ([])
        getInput()
    # If n == 0, list with 0.
    elif n==0: 
        print([0])
        getInput()
    else:
        # Initialize our list of Fibonacci numbers found so far.
        fib = [0,1]
        # Initialize result.
        result = 0
        while result <= n:
            # Use the previous two values to generate and record the next value.
            result = fib[-1] + fib[-2]
            # Add the newest value to the list we're creating.
            fib.append(result)
        print(fib[:-1])
        getInput()

def findIthFibNumber():
    # Return the ith Fibonacci number.
    n = int(input("You've asked for the ith Fibonacci number. What is i? "))
    # If n < 0, invalid input.
    if n<0:
        print("ERROR: Illegal value entered.")
        getInput()
    # If n == 0, return n.
    elif n==0: 
        print(n)
        getInput()
    else:
        # Initialize fib1 and fib2 with the first two Fibonacci numbers.
        fib1, fib2 = 0, 1
        # Initialize our list of Fibonacci numbers found so far.
        fibs = [0, 1]
        # Use the previous two values to generate and record the next value.
        for counter in range(2, n+1):
            # Update fib1 and fib2 with their new values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're creating.
            fibs.append(fib2)
        print(fibs[-1])
        getInput() 
    
def firstNFibNumbers():
    # Return a list of the first n Fibonacci numbers.
    n = int(input("You've asked for the first N Fibonacci numbers. What is N? "))
    # If n < 0, invalid input.
    if n < 0:
        print(ERRORVALUE)
        getInput()
    # If n == 0, return the empty list.
    if n == 0:
        print("[]")
        getInput()
        #return []
    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        print("[0]")
        getInput()
        #return [0]
    elif n == 2:
        print("[0, 1]")
        getInput()
    # Here we know that n is at least 2.
    else:
        # Initialize fib1 and fib2 with the first two Fibonacci numbers.
        fib1, fib2 = 0, 1
        # Initialize our list of Fibonacci numbers found so far.
        fibs = [0, 1]
        # Use the previous two values to generate and record the next value.
        for counter in range(2, n):
            # Update fib1 and fib2 with their new values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're creating.
            fibs.append(fib2)
        print(fibs)
        getInput()
        #return fibs

def getInput():
    # Displays blank line.
    print()
    # Asks user which command they would like and sets up tests for each command entry.
    userInput = input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): ")
    while True:
        if userInput == ZERO:
            print()
            print("Thanks for using the Fibonacci Laboratory!  Goodbye.")
            exit()
            break
        elif userInput == ONE:
            firstNFibNumbers()
        elif userInput == TWO:
            findIthFibNumber()
        elif userInput == THREE:
            fibNumbersLessOrEqualN()
        elif userInput == FOUR:
            fibNumCountLessOrEqualN()
        elif userInput == FIVE:
            largestFibNumsTotallingN()
        elif userInput == SIX:
            availableCommands()
            print()
            userInput = input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): ")
        else:
            print(ERRORCOMMAND)
            print()
            availableCommands()
            print()
            userInput = input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): ")
            
def availableCommands():
    # Displays a list of each command and their tasks
    print("The following commands are available:")
    print("  0: Exit.")
    print("  1: List the first N Fibonacci numbers.")
    print("  2: Display the ith Fibonacci number (0-based).")
    print("  3: List the Fibonacci numbers less or equal to N.")
    print("  4: How many Fibonacci numbers are less or equal to N?")
    print("  5: Find a list of the largest Fibonacci numbers that add up to N.")
    print("  6: Display this help message.")
    
# Main function for welcome message and calls needed functions to begin utility.
def main():
    print()
    print("Welcome to the Fibonacci Number laboratory!")
    print()
    availableCommands()
    getInput()

main()
