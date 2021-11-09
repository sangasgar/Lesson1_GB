#1
name = "Hello world"
age = 33
money = 500.00
status = False
print(name)
print("Ваш возраст " + str(age))
name_your = input("Введите Ваше имя ")
print("Привет " + name_your)
status = str(input("Вы женаты. Напишите да или нет "))
if status == "да":
    status = True
else:
    status = False
print(status)

#2
time = int(input("Введите время в секундах "))
time_hour = time // 3600
time_minutes = time % 3600
time_minutes = time_minutes // 60
time_seconds = time - (time_minutes * 60) - (time_hour * 60 * 60)
print(f"Время {time_hour} часов {int(time_minutes)} минут {time_seconds} секунд" )

#3
num_user = input("Введите число ")
num_user1 = num_user + num_user
num_user2 = num_user + num_user + num_user
num_user = int(num_user) + int(num_user1) + int(num_user2)
print(num_user)

#4
num_user_find = input("Введите целые положительные числа ")
count = 0
result = 0
while count < len(num_user_find):
      if  result < int(num_user_find[count]):
             result = int(num_user_find[count])
      count = count + 1
print(f"Наибольшее число {result}")

#5

Q = int(input("Введите выручку "))
C = int(input("Введите издержки "))
if Q > C:
    profitability = Q-C
    Rent = profitability/Q
    print(f"Вы имеете {profitability} прибыли")
    worker = int(input("Сколько у вас сотрудников "))
    print(f"{profitability/worker} профит на одного сотрудника.")
elif Q == C:
    print("Не плоха")
else:
    print("Вы не рентабельны")

#6
a = float(input("Введите результат в первый день "))
b = float(input("Введите резултат которого нужно достич "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
    print(f" {day} день: {a}")
print(f"на {day} день спортсмен достиг результата — не менее {b} км.")