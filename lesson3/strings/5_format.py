# Python підтримує кілька способів форматування рядків:

# Використання оператора %:
name = "Alice"
age = 30
formatted_str = "Привіт, %s! Тобі %d років." % (name, age)
print(formatted_str)


# Використання методу str.format():
name = "Bob"
age = 25
formatted_str = "Привіт, {}! Тобі {} років.".format(name, age)
print(formatted_str)


#Використання f-строк (з Python 3.6 і вище):
name = "Charlie"
age = 35
formatted_str = f"Привіт, {name}! Тобі {age} років."
print(formatted_str)
