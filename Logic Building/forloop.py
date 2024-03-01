
#TODO: Question 1: Sum of Natural Numbers: Write a program that uses a for loop to calculate the sum of the first N natural numbers.

def sumofNnaturalNumbers(N):
    if N == 1 or N == 0:
        return N
    else:
        total = 0
        for element in range(1, N+1):
            total += element

        return total

    

print(sumofNnaturalNumbers(1))

#TODO: Question 2: check Prime: Use a for loop to determine whether a number N is prime

def checkPrime(N):
    if N == 0 or N == 1:
        return False
    else: 
        for element in range(2, N):
            if N % element == 0:
                return False
        return True
    
print(checkPrime(1))
print(checkPrime(31))

#TODO: Question 3: Fibonacci Sequence: Write a program that prints the first N numbers of the Fibonacci sequence using a for loop.

def fibonacci():
    pass

#TODO: Question 4: Factorial Calculation: Write a function that uses a for loop to calculate the factorial of a given number N.

def factorial(N):
    fact = 1
    if N == 0 or N == 1:
        return N
    else: 
        for element in range(1, N+1):
            fact = fact * element

        return fact
    
print(factorial(5))

