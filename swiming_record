# Въвеждане на рекорда, разстоянието и времето за плуване на 1 метър
record = float(input())
distance = float(input())
time_per_meter = float(input())

# Изчисление на времето, нужно за плуването на цялото разстояние
total_time = distance * time_per_meter

# Изчисление на забавянето поради съпротивлението на водата
water_resistance_delay = (distance // 15) * 12.5

# Общо време
total_time += water_resistance_delay

# Проверка дали Иван е подобрил рекорда
if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(total_time - record):.2f} seconds slower.")
