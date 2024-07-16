#task 1
# for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)


#task 2
def celsius_to_fahrenheit(C):
    return (C * 9/5) + 32

def fahrenheit_to_celsius(F):
    return (F - 32) * 5/9

def main():
    celsius = 60
    fahrenheit = 45
    print(f'{celsius}°C is {celsius_to_fahrenheit(celsius)} in Fahrenheit')
    print(f'{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)} in Celsius')

main()


#task 3
import random

def main():
    number = random.randint(1, 9)
    guess = None
    
    while guess != number:
        guess = int(input('Guess a number between 1 and 9: '))
        if guess == number:
            print('Well guessed!')
main()


#task 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print()

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print('*', end='')
    print()


#task 5
word = input("Enter a word: ")
reverse = ''

for i in range(len(word) - 1, -1, -1):
    reverse += word[i]
print("Reverse of the word is: ", reverse)


#task 6
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_even = 0
count_odd = 0

for i in numbers:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)


#task 7

dataList = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {11:'V', 12:'A'}]

for i in dataList:
    print(i, type(i))


#task 8
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=' ')

#task 9
    a, b = 0, 1
while b < 50:
    print(b, end=' ')
    a, b = b, a + b

#task 10
    for num in range(1, 50):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#task 11
def create_table(i, j):
    rows = i
    columns = j
    arr = []
    
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i * j)
        arr.append(row)
        
    return arr

def print_table(table):
    for row in table:
        for cell in row:
            print(cell, end=' ')
        print()

def main():
    # Taking user input for rows and columns
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    
    table = create_table(rows, columns)
    print_table(table)
    
main()

#task 12
def main():
    lines = []
    
    while True:
        line = input("Enter a line: ")
        
        if line == "":
            break
        
        lines.append(line)
    
    for line in lines:
        print(line.lower())
        
main()

#task 13

def main():
    binary_numbers = input("Enter a sequence of comma separated 4 digit binary numbers: ")
    binary_numbers = binary_numbers.split(',')
    
    for binary_number in binary_numbers:
        decimal_number = int(binary_number, 2)
        
        if decimal_number % 5 == 0:
            print(binary_number, end=', ')

main()

#task 14

def main():
    string = input("Enter a string: ")
    
    letters = 0
    digits = 0
    
    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    
    print(f"Letters {letters}")
    print(f"Digits {digits}")
    
main()

#task 15

def main():
    password = input("Enter a password: ")
    
    if len(password) < 6 or len(password) > 16:
        print("Password must be between 6 and 16 characters")
        return
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True
    
    if has_lower and has_upper and has_digit and has_special:
        print("Valid password")
    else:
        print("Invalid password")
        
main()
