amount = int(input("Enter your amount: "))
dis = int(input("Enter your discount: "))

minus = amount * dis / 100

final_amount = amount - minus

print(f'original price {amount}')
print(f'discount {minus}')
print(f'Payable amount {final_amount}')