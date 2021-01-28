# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# https://drive.google.com/file/d/1HukSj3fYH8tXmKDe1MjwcJUlp58W1QMs/view?usp=sharing
year = int(input("Введите год "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"год високосный")
    else:
        print(f"год високосный")
else:
    print(f"год не високосный")