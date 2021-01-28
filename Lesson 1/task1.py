# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1HukSj3fYH8tXmKDe1MjwcJUlp58W1QMs/view?usp=sharing

number = int(input("Введите трёхзначное число"))
a = number%10
number = number//10
b = number%10
number = number//10
c = number%10
print(a+b+c)
print(a*b*c)