s = input("Введіть закодований рядок (наприклад, 3ab4c2CaB): ")

result = []
num_str = ""

# Розбираємо кожен символ рядка
for char in s:
    if char.isdigit():
        num_str += char  # Накопичуємо цифри для кількості
    else:
        count = int(num_str) if num_str else 1
        result.append(char * count)
        num_str = ""  # Скидаємо лічильник

print("Декодований рядок:")
print("".join(result))