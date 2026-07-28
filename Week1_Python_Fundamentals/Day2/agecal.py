date = int(input("Enter your birth date: "))
mon = int(input("Enter your birth mon: "))
year = int(input("Enter your birth year: "))

td = 27
tm = 7
ty = 2026

if mon < tm:
    age = ty - year
    print(f'You are ${age} years old')
elif mon > tm:
    age = ty - year - 1
    print(f'You are ${age} years old')
elif mon == tm and td > date:
    age = ty - year 
    print(f'You are ${age} years old')
elif mon == tm and td < date:
    age = ty - year - 1