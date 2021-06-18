def splitting(input):
    output = input.split('e')
    return output

print(splitting('bananas are not fantastic'))


def joining(input):
    output = "Luke".join(input)
    return output
    
#print(joining(['h', 'ell', 'o']))

def replacing(input):
    output = input.replace('e', 'i')
    return output

#print((replacing('Lisa is a smelly goat and I dont like her')))

def for_string(input):
    listy = []
    for letter in input:
        listy.append(letter)
        return listy
    output = listy.replace('e', 'a')
    return output

#print(for_string("Yeehaw"))

def index_string(input):
    return input[3]


def index_range(input):
    return input[3:5]

print(index_range("12345678"))

def the_range():
    output = []
    for number in range(1, 10, 2):
        output.append(number)
    return output

print(the_range())