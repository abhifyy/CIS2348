"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input('Enter amount of water (in cups):\n'))
nectar = float(input("Enter amount of agave nectar (in cups):\n"))
serving = float(input("How many servings does this make?\n"))
print()
print(f'Lemonade ingredients - yields {serving:.2f} servings')
print(f'{lemon:.2f} cup(s) lemon juice')
print(f'{water:.2f} cup(s) water')
print(f'{nectar:.2f} cup(s) agave nectar\n')

n = float(input('How many servings would you like to make?\n'))
print()
print(f'Lemonade ingredients - yields {n:.2f} servings')
print(f'{(n*1/3):.2f} cup(s) lemon juice')
print(f'{(n*8/3):.2f} cup(s) water')
print(f'{(n*5/12):.2f} cup(s) agave nectar')

print(f'\nLemonade ingredients - yields {n:.2f} servings')
print(f'{(n*1/3)/16:.2f} gallon(s) lemon juice')
print(f'{(n*8/3)/16:.2f} gallon(s) water')
print(f'{(n*5/12)/16:.2f} gallon(s) agave nectar')
