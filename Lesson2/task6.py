# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

num = random.randint(0, 100)
print("Отгадайте число от 0 до 100 за 10 попыток")
for i in range(1, 10 + 1):
    answer = int(input(f'Попытка {i}: '))
    if num < answer:
        print('Число меньше')
    elif num > answer:
        print('Число больше')
    else:
        print(f'Вы угадали с {i}-й попытки')
        break
else:
    print(f'Поражение. Было загадано {num}')
print('После')
