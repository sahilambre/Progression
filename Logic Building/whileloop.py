
#TODO: Question 1: Find Power of Two: Write a program that finds the highest power of 2 less than or equal to a given number N using a while loop.

def highestPower(number):
    counter = 0
    while 2 ** counter <= number:
        counter += 1
    return counter - 1

print(highestPower(9))

#TODO: Question 2: Collatz Conjecture: Implement the Collatz conjecture and count the steps it takes to reach 1 starting from a given number N.

def collatzConjecture(N):
    steps = 0
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = 3 * N + 1
        steps += 1
    
    return steps

print(collatzConjecture(6))