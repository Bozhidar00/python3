# Въвеждане на бюджета и количеството видеокарти, процесори и рам памет
budget = float(input())
num_graphics_cards = int(input())
num_processors = int(input())
num_ram_memory = int(input())

# Изчисление на цената на видеокартите, процесорите и рам памет
graphics_card_price = num_graphics_cards * 250
processor_price = (35 / 100) * graphics_card_price * num_processors
ram_memory_price = (10 / 100) * graphics_card_price * num_ram_memory

# Обща цена
total_price = graphics_card_price + processor_price + ram_memory_price

# Проверка за отстъпка
if num_graphics_cards > num_processors:
    total_price -= total_price * 0.15

# Проверка дали бюджетът е достатъчен
if total_price <= budget:
    left_budget = budget - total_price
    print(f"You have {left_budget:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
