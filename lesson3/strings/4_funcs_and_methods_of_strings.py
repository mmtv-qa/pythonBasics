
# Python надає безліч корисних функцій та методів для роботи із рядками. Ось декілька з них разом з прикладами:

# len(string): Повертає довжину рядка.
text = "Hello, World!"
length = len(text)  # length = 13


# string.upper() Перетворює рядок у верхній регістр.
text = "Hello, World!"
uppercase_text = text.upper()  # uppercase_text = "HELLO, WORLD!"


# string.lower(): Перетворює рядок у нижній регістр.
text = "Hello, World!"
lowercase_text = text.lower()  # lowercase_text = "hello, world!"
print(lowercase_text.capitalize())


# string.strip() Видаляє пробіли із початку та кінця рядка.
text = "  Hello, World!  "
stripped_text = text.strip()  # stripped_text = "Hello, World!"


# string.split(separator) Розбиває рядок на список підстрок за роздільником.
text = "apple, banana, cherry"
fruits = text.split(", ")  # fruits = ["apple", "banana", "cherry"]


# string.replace(old, new) Замінює всі входження підстроки old на new.
text = "I like apples. Apples are great."
new_text = text.replace("apples", "bananas")  # new_text = "I like bananas. Bananas are great."


# string.find(substring) Знаходить перше входження підстроки substring та повертає його індекс.
# Якщо не знайдено, повертає -1.
text = "Hello, World!"
index = text.find("World")  # index = 7
