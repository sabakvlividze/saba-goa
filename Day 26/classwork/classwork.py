#1)
def numbers (start,end):
    for i in range (start,end):
        print(i)

numbers(1,5)
numbers(6,10)

#2)

def calculate_sum (start,end):
    result = 0
    for i in range (start,end):
        result = result + i
    print(result)

calculate_sum(2,5)



#3)

def calculate_arithmetic(start, end):
    numbers = []

    for i in range(start, end):
        numbers.append(i)
    
    result = sum(numbers) / len(numbers)

    print(result)

calculate_arithmetic(5, 11)

#4)

def print_char (name, index):
    print(name[index])

print_char("saba",2)

#6) 
def calculate_sum(start,end):
    result = 0
    for i in range(start,end):
        result += i
    print(result)

    return (calculate_sum)
#7)
def sum_of_numbers(numbers_list):
    total = 0
    
    for i in numbers_list:
        total = total + i
        
    return total
    
var1 = sum_of_numbers([1, 2, 3, 4, 5])
print(var1)

var2 = sum_of_numbers([6, 7, 8, 9, 10])
print(var2)








# def sum (num1,num2):
#     result = 0
#     for i in range(num1,num2):
#         result = num1 + num2
#         return result
#     print(result)

# return(sum)    





          




   
