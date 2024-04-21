#1)
for i in range (1,51):
    if i % 5 == 0:
        print(i)
#2)
for i in range(2,21):
    if i % 2 == 0:
        print(i)

#3)
final_product = 1        
for i in range(5,11):
    final_product *= i
    print(final_product)
#4)
num = int(input("enter your number"))
sum = 1
for i in range (1,num +1):
    sum *= i
    print(sum)
#5)
num = int(input("enter your number")) 
if num %2 == 0:
    print(num/2)
else:
    print(num*3+1)    
#6)
num = 10
while num>=1:
    print(num)
    num -= 1
#7)
enter = input("enter your passwod")
while enter!= "quit":
    enter = input("enter your passwod")
print("Access Granted")    
#8)
i = 10
finish = 21
while i < finish:
    if i % 2 == 0:
        print(i)
    i += 1   
#9)
num = int(input("enter your number"))         
while num <=0:
    num = int(input("enter your number"))
print("accsess Granted")
#10)
num = 1
while num <=10:
    print(num**3)
    num += 1



