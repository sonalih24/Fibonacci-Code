# Fibonacci-Code
This code shows a built utility by myself that allows the user to generate a list of the first N Fibonacci numbers, find and display the ith Fibonacci number, generate a list of Fibonacci numbers up to and possibly including the positive integer N, and find a list of Fibonacci numbers that add up to a non-negative integer N.
My program prints out an initial welcome message and a list of available commands. I have assigned 7 possible commands, which will be entered as a numeral between 0 and 6. Here are the available commands:
  0: Exit.
  1: List the first N Fibonacci numbers.
  2: Display the ith Fibonacci number (0-based).
  3: List the Fibonacci numbers less or equal to N.
  4: How many Fibonacci numbers are less or equal to N?
  5: Find a list of the largest Fibonacci numbers that add up to N.
  6: Display this help message. 
Depending on the command, the user is asked to specify the parameter (N or i). The code then computes and prints the answer, prints an error message and the menu, or prints a goodbye message and exit. It is fair to assume that the user will only input integers, but not that they're in the correct ranges. If they're not, an error message will be printed. 
