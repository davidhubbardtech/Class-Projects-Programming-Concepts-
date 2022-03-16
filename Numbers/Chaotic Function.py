# File: David_Hubbard_Chaotic_Function_EX5.py
# A chaotic function that includes a user determined n value

def chaos():
    print("This program illustrates a chaotic function")
    print("This code was entered by David Hubbard")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        print(x)
        x = 2.0 * x * (1 - x)
        print("i=", i)
        print(x)
    print("I am done")
    print(input("Hit ENTER to exit"))

chaos()