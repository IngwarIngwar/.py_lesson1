t = int(input('Введите время в секундах - '))
seconds = t % 60
hours = t // 3600
minutes = int((t / 60) - (hours * 60))
print(f"{hours:02}:{minutes:02}:{seconds:02}")