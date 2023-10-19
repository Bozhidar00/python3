hour = int(input("Въведете час (0-23): "))
minute = int(input("Въведете минути (0-59): "))

total_minutes = hour * 60 + minute
total_minutes += 15

new_hour = total_minutes // 60
new_minute = total_minutes % 60

hour_str = str(new_hour).zfill(2)
minute_str = str(new_minute).zfill(2)

print(f"{hour_str}:{minute_str}")
