print("========== Python Utility App ==========")
print("1. Calculator")
print("2. BMI calculator")
print("3. Tempreture converter")
print("4. Discount Calculator")
print("5. Age Calculator")
print("6. Exit")

choose = int(input("Choose an option: "))

if choose == 1:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    operator = input("Choose an Operator (+,-,*,/): ")

    if operator == "+":
        c = a + b
        print(c)
    elif operator == "-":
        c = a - b
        print(c)
    elif operator == "*":
        c = a * b
        print(c)
    elif operator == "/":
        c = a / b
        print(c)

elif choose == 2:
    w = int(input("Enter your weight: "))
    h = float(input("Enter your height: "))
    htw = h * h
    bmi = w / htw
    final_bmi = round(bmi,2)
    print(f'Final BMI is: {final_bmi}')

    if final_bmi <= 18.5:
        print("Categories : Underweight")
    elif final_bmi > 18.5 and final_bmi <= 24.9:
        print("Categories : Normal weight")
    elif final_bmi > 25 and final_bmi < 29.9:
        print("Categories : Overweight")
    elif final_bmi >= 30:
        print("Categories : Obese")

elif choose == 3:
    print("This is for Celcius to Fahrenheit")
    c = int(input("Enter Celcius: "))
    fc = c * 1.8
    f = fc + 32

    print(f'{c}c converted into {f}f')

elif choose == 4:
    o = int(input("Enter Original price: "))
    d = int(input("Enter Discount: "))
    da = o * d / 100
    Final_amount = o - da
    print(f'The discount is {da}')
    print(f'The amount after discount is {Final_amount}') 

elif choose == 5:
    mon = int(input("Enter your born month: "))
    year = int(input("Enter your born year: "))

    current_mon = 7
    current_year = 2026

    if mon > current_mon:
        c = current_year - year - 1
        print(f'You are {c} years old')
    elif mon < current_mon:
        c = current_year - year
        print(f'You are {c} year old')