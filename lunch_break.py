# Въвеждане на името на сериала, продължителността на епизода и продължителността на почивката
serial_name = input()
episode_duration = int(input())
break_duration = int(input())

# Изчисление на времето за обяд и времето за отдих
lunch_time = break_duration * 1/8
relax_time = break_duration * 1/4

# Изчисление на оставащото свободно време
free_time = break_duration - lunch_time - relax_time

# Проверка дали времето е достатъчно да изгледате епизода
if free_time >= episode_duration:
    print(f"You have enough time to watch {serial_name} and left with {round(free_time - episode_duration)} minutes free time.")
else:
    needed_time = episode_duration - free_time
    print(f"You don't have enough time to watch {serial_name}, you need {round(needed_time)} more minutes.")
