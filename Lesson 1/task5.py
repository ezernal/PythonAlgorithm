#Пользователь вводит две буквы.
#Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1HukSj3fYH8tXmKDe1MjwcJUlp58W1QMs/view?usp=sharing

a = ord(input("Введите 1-ю букву: "))
b = ord(input("Введите 2-ю букву: "))
a = a - ord("a") + 1
b = b - ord("a") + 1
print("Позиции: %d и %d" % (a, b))
print("Позиции: %d и %d" % (a, b))