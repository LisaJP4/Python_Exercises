

#### THESE ARE NOT MY ANSWERS TO THE PYTHON ASSESSMENT: THESE ARE THE SOLUTIONS (GONE OVER AFTER THE EXAM)
# FOR MY ANSWERS - CHECKED FORKED ASSESSMENT2 REPO


# given a string, return a string whre for every char n the original string, thre are three chars

# one("The") >>>> "TTThheee"

#LOGIC
# output string 
# iterate through input string
# add 3* each character to output string

def one(string):
    output = ""
    for character in string:
        output += character*3
    return output

# write a function which returns the boolean True if the input is only divisible by one and itself
# prime number - can use math module
# if remainder = 0  for any of them, return false 

def two(number):
    for i in range(2, number):
        if number % i ==0:
            return False
        return True

# write a function which takes an integer input which returns the sum of the int+intint+intintint+intintint...

#logic
#make all four numbers strings
# use multiply operator to concatenate string
#make integers and sum

def three(a):
    a = str(a)
    a2 = a*2
    a3 = a*3
    a4 = a*4
    output = int(a) + int(a2) + int(a3) + int(a4)
    return output


    # given two strings of equal length, merge them into one string
    # ie. "string, frdige" >>>> "sftrrdiingge"

    def four(string1, string2):
        output = ""
        for i in range(len(string1)):
            output += string1[i]+string[i]
        return output

# write a function that randomly generates a list with 5 even numbers between 100 and 200 inclusive

#logic
# can ensure even by multiplying by 2

from random import randint
def five():
    output = []
    for i in range(5):
        number = randint(50,100)
        output.append(2*number)
    return output

# given a string, return the Boolean True f it ends in ;py' and false if not

def six(string):
    string = string.lower()
    if string[-2:1] == 'py':
        return True:
    else:
        return False 

#given three ints, a b c, one of them is small, one is medium and one is large. return the boolean true if the three values are evenly space
# e.g (2, 4, 6) >>> True
# 4,6, 2 >>>>true 
# 4, 50, 9 >>>> False

#Get the numbers into a list, sort it, check the differences, true if differences are equal, false if not

def seven(a, b, c):
    nums = [a, b, c]
    nums.sort()
    difference1 = nums[1] - nums[0]
    difference2 = nums[2] - nums[1]
    if difference1 == difference2:
        return True
    else:
        return False

#given a string and an integer, n, return a string that removes n letters form the 'middle' of the string
# logic
# make string a list
# find length of list
#find start of middle
#find end of middle
#set start-end = ''
# join back to a string

def eight(string, a):
    letters = []
    for characters in string:
        letters.append(character)
    length = len(string)
    start = int((length - a)/2)
    end = length - start
    for i in range(start, end):
        letters[i] = ''
    output = ''.join(letters)
    return output

def nine(string1, string2):
    if len(string1) >= len(string1):
        big = string1
        small = string2
    else:
        big = string1
        small = string2

    list = []
    for i in big:
        list.append(i)

    for letter in small: 
        match = False
        index = 0

        while index < len(list) and match == False:
            if letter == list[index]:
                list[index]:
                list[index] = ''
                match = True
            index += 1

        if match == False:
            return False 

        return True

