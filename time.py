# Запрашиваем время по частям
hours = int(input("Введите часы: "))
minutes = int(input("Введите минуты: "))
seconds = int(input("Введите секунды: "))

# Считаем общее количество секунд
total_seconds = hours * 3600 + minutes * 60 + seconds

print(f"Общее время в секундах: {total_seconds}")