# if-elif-else

true = True
false = False

age_str = input("Скільки вам років? ")
age = int(age_str)

if age >= 18:
    print("Ви повнолітні.")
elif age <= 0:
    print("Певно, ви не ще не народились")
elif False:
    print("Я ніколи не відпрацюю")
else:
    print("Ви неповнолітні.")



print("go next")