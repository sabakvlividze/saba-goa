#1)
def manual_max(number_list):
    max_number = number_list[0]

    for number in number_list:
        if number > max_number:
            max_number = number

    return max_number

print(manual_max([4,5,2,8,9,2,1,6,4]))    

#2)
def manual_min(number_list):
    min_number = 4

    for number in number_list:
        if min_number > number:
            min_number = number
    
    return min_number

print(manual_min([2,5,3,6,3,8,9,2,1]))

#3)
def manual_index(numbers_list, search_value):
    if search_value not in numbers_list:
        return -1
    
    for i in range(0,len(numbers_list)):
        if search_value == numbers_list[i]:
            return i

manual_index()
            
    