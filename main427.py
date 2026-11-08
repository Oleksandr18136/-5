# Зчитуємо список цілих чисел через пробіл
data = list(map(int, input("Введіть цілі числа через пробіл: ").split()))

# Обчислюємо необхідні показники
min_val = min(data)
max_val = max(data)
count = len(data)
avg_val = sum(data) / count

# Виводимо результати
print(f"Найменше число: {min_val}")
print(f"Найбільше число: {max_val}")
print(f"Кількість чисел: {count}")
print(f"Середнє значення: {avg_val}")