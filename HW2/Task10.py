# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input("Введите количество монет: "))
i = 0
m = 0
k = 0
print("Введите поочередно монеты, которые лежат на столе (герб - 1, решка - 0): ")
while i < n:
    coin = int(input())
    if coin == 1:
        m = m + 1
    else:
        k = k + 1
    i=i+1

if m > k:
    count = k
else:
    count = m

print(f"Минимальное количество монет, которые нужно перевернуть: {count}")