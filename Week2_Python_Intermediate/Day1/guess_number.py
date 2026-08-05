import random

secret_code = random.randint(1,101)
attempt = 0
while True:

    geuss = int(input(f'Geuss a number between 1 to 100: '))
    attempt += 1

    if geuss > secret_code:
        print(f'Geuss Smaller')
    elif geuss < secret_code:
        print(f'Geuss Higher')
    elif geuss == secret_code:
        print(f'Currect')
        print(f'Total attempts: {attempt}')
