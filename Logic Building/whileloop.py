
#TODO: Question 1: Find Power of Two: Write a program that finds the highest power of 2 less than or equal to a given number N using a while loop.

def highestPower(number):
    counter = 0
    while 2 ** counter <= number:
        counter += 1
    return counter - 1

print(highestPower(9))