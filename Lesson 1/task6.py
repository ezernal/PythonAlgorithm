#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# https://drive.google.com/file/d/1HukSj3fYH8tXmKDe1MjwcJUlp58W1QMs/view?usp=sharing

n = int(input("Введите номер буквы в алфавите: "))
n = ord("a") + n - 1
print("Это буква", chr(n))