import sys

balance = 0
print("Введіть транзакції (наприклад, D 100 або W 200). Для завершення натисніть Enter на порожньому рядку:")

# Порядковий ввід транзакцій до порожнього рядка
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    action, amount = line.split()
    amount = int(amount)
    
    if action == 'D':
        balance += amount
    elif action == 'W':
        balance -= amount

print(f"Підсумковий баланс: {balance}")