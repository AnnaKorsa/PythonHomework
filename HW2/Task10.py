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