#1)
names = ["saba", "luka", "gio", "mate","levani"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
#2)
names = ["saba", "luka", "gio", "mate","levani"]

for name in names:
    print(name)   
# 3)
numbers = [1,2,3,4,5,6,7,8,9,10]

result = 0

for num in numbers:
    result = result + num

print(result)    

numbers = [1,2,3,4,5,6,7,8,9,10]

result = 1

for num in numbers:
    result = result * num

print(result)   
#4)
numbers = [1,2,3,4,5,6,7,8,9,10]

result = 0

for num in numbers:
    if num % 2 == 0:
        result = result + num
        
print(result)        
#5)
numbers = [1,2,3,4,5,6,7,8,9,10]

result = 0
odd_multiple = 1

for num in numbers:
    if num % 2 != 0:
        result = result + num
        odd_multiple = odd_multiple * num

print(result)
#6)
My_name = ["s","a","b","a"]

for i in My_name:
    print(i)
#7)
name = "Saba"
even_indexes_string = ''
        # 0 1 2 3 4 5
for i in range(0,len(name)):
    if i %2 == 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)        
      


 



     