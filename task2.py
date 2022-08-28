name = input("Введіть Ваше ім'я: ").capitalize()
age = input("Скільки Вам років: ")
age1 = int(age) + 1
if not age.isdigit() or not name.isalpha():
    print("перевірте типи вхідних даних")
else:
    print(f'Hello {name}, on your next birthday you’ll be {age1} years')