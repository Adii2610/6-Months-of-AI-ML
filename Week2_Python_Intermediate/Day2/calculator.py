#---------------Calculator--------------

print(f'1. Addition')
print(f'2. Substraction')
print(f'3. Multiplication')
print(f'4. Divide')

operation = int(input(f'Choose your operation: '))

first = int(input(f'Enter your first number: '))
second = int(input(f'Enter your second input: '))

def add(a,b):
    return a + b

def substraction(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b


if operation > 4 or operation < 1:
    print(f'Invalid Input! you need to choose only 1 to 4 operations')
else:
    if operation == 1:
        print(add(first, second))
    elif operation == 2:
        print(substraction(first,second))
    elif operation == 3:
        print(multiply(first, second))
    elif operation == 4:
        if second == 0:
            print("you cannot choose 0 in second number")
        else:
            print(divide(first, second)) 