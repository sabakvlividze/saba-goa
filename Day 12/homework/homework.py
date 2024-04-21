#1)
budget = int(input("What is your budget: "))
cost = int(input("Please enter cost: "))

if budget >= cost:
    print("You have enough money")
else:
    print("You dont have enough money") 
#2)
registered_password = "luka1234"

password = input("please enter your password: ")

while password != registered_password:
    password = input("please enter your password again: ")
    if password ==  registered_password:
        print("you have accsses on your account" )
    else:
        print("you have entered a wrong password, please try again")  
#3)
start = int(input("Please enter starting value: "))
end = int(input("Please enter ending value: "))
step = int(input("Please enter step value: "))
2
for i in range(start,end,step):
    print(i)

#4)
#?

#5)
operation = input("please enter your operation (+,-,*,/): ")
num1 = int(input("Please enter first number:"))
num2 = int(input("Please enter second number:"))

if operation == "+":
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("operation is not valid")


    



