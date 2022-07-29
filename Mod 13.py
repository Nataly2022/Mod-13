# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

S = 0
n = 1
conc_tiсket = 990   # льготный билет
full_tiсket = 1390  # полный билет

tiсkets = int(input("Введите количество билетов: "))
while True:
    age = int(input(f"Введите возраст {n} посетителя: "))
    if age < 18:
        S = S
    elif 18 <= age <= 25:
        S += conc_tiсket
    else:
        S += full_tiсket
    n += 1
    if n > tiсkets:
        break
if tiсkets > 3:
    print(f"Сумма к оплате со скидкой 10%: {S} руб.")
else:
    print(f"Сумма к оплате: {S} руб")
