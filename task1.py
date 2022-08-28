import random
s = input("Введіть число: ")
if not s.isdigit():
    print("тільки числа!")
else:
    computer = random.randint(1,11)
    if computer == s:
        print(f"Ви вгадали число. Число загадане комп'ютером - {computer}")
    else:
        print(f"Фортуна не на Вашому боці. Число комп'ютера {computer}")