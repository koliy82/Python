from calendar import monthrange

print("Введите год:")
year = int(input())
result = 0
for i in range(1, 13):
    days = monthrange(year, i)[1]
    print(f"В {i} месяце {days} дней")
    for j in range(1, days+1):
        one = (int)(j/10)
        two = (int)(j%10)
        print(f"Число {days} one = {one} two = {two}")
        result+=one+two
    print(result)
print(f"Сумма всех чисел в {year} году: {result}")