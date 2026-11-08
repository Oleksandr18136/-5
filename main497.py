a = input("Введіть основний рядок A: ")
b = input("Введіть підрядок B для пошуку: ")

positions = []
start = 0

# Шукаємо всі входження підрядка
while True:
    pos = a.find(b, start)
    if pos == -1:
        break
    positions.append(pos + 1)  # Нумерація позицій з 1
    start = pos + 1

# Виводимо результат
if positions:
    print("Позиції входження:", *positions)
else:
    print("Результат:", -1)