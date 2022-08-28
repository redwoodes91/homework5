from random import choice
from string import ascii_uppercase
s = ''.join(choice(ascii_uppercase) for i in range(5))
l = [i for i in s]
print('строка -',s)
print("посимвольно -", l)