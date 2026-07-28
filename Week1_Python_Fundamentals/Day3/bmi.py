w =  int(input("Enter your weight: "))
h = float(input("Enter your height in meters: "))

htw = (h * h)
bmi = w / htw
final = round(bmi,2)

print(f'BMI {final}')

if final <= 18.5:
    print('Category = Underweight')
elif final > 18.5 and final < 24.9:
    print('Category = Normal weight')
elif final > 25 and final < 29.9:
    print('Category = Overweight')
elif final >= 30:
    print('Category = Obese')