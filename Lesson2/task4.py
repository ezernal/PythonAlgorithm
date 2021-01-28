# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


number = int(input("Сколько элементов сложить: "))
calk = 1
sumber = 0
for zir in range(number):
    sumber += calk
    calk /= -2
print(sumber)