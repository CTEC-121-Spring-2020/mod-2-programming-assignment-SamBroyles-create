"""
CTEC 121
Sam Broyles
Mod 2 Programming assignment
Programming assignment homework
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from math import *
def main():
    """
    # assignment statements
    theA = int(15)
    theB = float(6.9)
    theC = "It was me Sam"
    print()
    print("Look at these cool numbers: ", theA, theB)
    print()
    print("Who made these numbers?", theC)
    print()

    # end and sep
    print("Sam", "Broyles", sep="_")
    print()
    print("When it gets really cold outside, ", end=(""))
    print("its probably winter.")
    print()

    # escape characters
    print("\ngive me some space", "\n")
    print("\tgive me some space", "\n")
    print("he said \"""give me some space\"")
    print()

    # getting user input
    # name input will accept anything
    name = input("What is your name? ")
    print("Hello ", name)
    print()
    # int input does not accept decimals or letters
    number = int(input("Favorite number? "))
    print(number, "nice choice")
    print()
    # float also does not accept words
    partial = float(input("Second favorite number? "))
    print(partial, "looks better.")
    print()
    # eval wont accept words or letters
    otherNumber = eval(input("Favorite math question? "))
    print("I know this one its", otherNumber)
    print()
   
    # simultaneous assignment
    add, sub = 10+3, 10-3
    print(add, sub)
    print()
    one, two = eval(input("Type two numbers seperated by a comma: "))
    print(one, two)
    print()
    
    # integer arithmetic
    print(5/2)
    print(5%2)
    
    # definite loop
    for i in [1, 6, 7, 8, 4, 15, 16, 1]:
        print(i)
    print()
    for j in range(11, 26, 3):
        print(j)
    
    # math library
    print()
    print(pi)
    print()
    #square root 
    print(int(sqrt(100)))
    print()
    #floor and ceiling function
    print(ceil(6.989274982))
    print(floor(6.989274982))
    print()
    #square 
    print(2**2)
    #cube
    print(10**3)
    print()
    
    #accumulator pattern
    #accumulator sum
    L = eval(input("Enter a number: "))
    M = eval(input("Enter another number: "))
    N = eval(input("Enter another number: "))
    O = eval(input("Enter yet another number: "))
    P = eval(input("Enter one final number: "))
    total = 0
    for Q in [L, M, N, O, P]:
        total = total + Q 
    print("your total is: ", total)
    """
    # accumulator sum of squares
    L = eval(input("Enter a number: "))**2
    M = eval(input("Enter another number: "))**2
    N = eval(input("Enter another number: "))**2
    O = eval(input("Enter yet another number: "))**2
    P = eval(input("Enter one final number: "))**2
    total = 0
    for Q in [L, M, N, O, P]:
        total = total + Q 
    print("your total is: ", total)

main()    