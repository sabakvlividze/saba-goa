#1)
def multiply(a, b):
  return a * b
#2)
def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    else:
        return "Odd"
#3)
def number_to_string(num):
    return str(num)
#4)
def solution(string):
    return string[::-1]
#5)
def positive_sum(arr):
    # Initialize a variable to store the sum of positive numbers
    total = 0
    
    # Iterate through the elements of the array
    for num in arr:
        # Check if the number is positive
        if num > 0:
            # Add the positive number to the total
            total += num
    
    # Return the sum of positive numbers
    return total