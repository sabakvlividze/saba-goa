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