# Въвеждане на бюджета, броя статисти и цената на облеклото
budget = float(input())
num_statists = int(input())
price_per_statist_clothing = float(input())

# Изчисление на сумата за декор
decor_cost = budget * 0.10

# Изчисление на сумата за облекло
clothing_cost = num_statists * price_per_statist_clothing

# Проверка за отстъпка при повече от 150 статисти
if num_statists > 150:
    clothing_cost *= 0.90

# Обща сума за филма
total_cost = decor_cost + clothing_cost

# Проверка дали бюджетът е достатъчен
if total_cost <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")