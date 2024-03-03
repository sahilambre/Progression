
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

#TODO: Question: Count Digits: Write a program that counts the number of digits in a given integer N using a for loop.

def countDigits(N):
    if N >= 0 and N < 10:
        return 1
    else:
        count = 0
        while N != 0:
            N = N // 10
            count = count + 1
        return count
    
print(countDigits(1234568))

def countDigits1(N):
    if N >= 0 and N < 10:
        return 1
    else:
        count = 0
        for element in str(N):
            if element.isdigit():
                count = count + 1
        return count
    
print(countDigits1(123))

#TODO: Question 6: Reverse an Array: Use a for loop to reverse the elements of an array.
#! recheck - debug
# def reverseArray(nums):
#     newList = []
#     for element in range(0, nums + 1, -1):
#         newList.append(nums[element])

#     return newList
# print(reverseArray([1,2,3,4,5,6]))

#TODO: Question 7: Find the Maximum: Implement a function that uses a for loop to find the maximum value in an array.

def findMax(arr):
    max = float('-inf')
    for element in arr:
        if element > max:
            max = element
    
    return max

print(float('-inf'))
print(findMax([1,2,33,4,5,6]))

#TODO: Question 8: Character Frequency: Write a program that uses a for loop to count the frequency of a specific character in a given string.

def countFrequency(input_string, target_char):
    counter = 0
    for letter in input_string:
        if letter == target_char:
            counter += 1
    
    return counter 

print(countFrequency('ssahil', 'z'))

#TODO: Question 9: Multiplication Table: Use a for loop to print the multiplication table of a given number up to N.

# def multiplyTable(number):
#     for element in range(1, number + 1):
#         total = 1
#         multiplication = number * element
#         total = multiplication
#         print(number, " x ",element, " = ", total)
#         total = 0

def multiplyTable(number):
    for element in range(1, number + 1):
        total = number * element
        print(number, " x ",element, " = ", total)
print(multiplyTable(4))

#TODO: Question 10: Sum of Array Elements: Write a function that calculates the sum of the elements in an integer array using a for loop.

def arraySum(arr):
    if len(arr) == 0:
        return 0
    else:
        total = 0
        for element in arr:
            total += element
        return total

print(arraySum([1,2,3,4,5,6]))
print(arraySum([1]))