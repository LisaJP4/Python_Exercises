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

