#Calculate the multiplication and sum of two numbers 

def multy(x, y):
    x = int(x)
    y = int(y)
    if x * y >= 1000:
        return x + y
    else: 
        return x * y


x = input("Enter your first number: ")
y = input("Enter your second number: ")
result = (multy(x, y))
print("Your number is", result)

# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate through the first 10 numbers and in each iteraction, also print the sum of the current and previous number

print("Printing current and previous number and their sum in range(10)")
previous_num = 0
for i in range(1, 11):
    x_sum = previous_num +i
    print("Current number", i, "Previous number", previous_num, " Sum: ", x_sum)
    previous_num = i



#Now, write the same function but instead of adding the numbers, it multiplies. Also, allow the user to enter their own numbers
def silly_sausage(x, y):
    previous_num = 0 
    x = int(x)
    y = int(y)
    for i in range(x, y):
        x_multi = previous_num*i
        print("Current number", i, "Previous number", previous_num, "Multiplied", x_multi)
        previous_num = i



x = input("Please enter a number")
y = input("Please enter a number")
result = silly_sausage(x, y)
