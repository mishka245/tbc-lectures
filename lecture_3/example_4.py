import random

number_1 = random.randint(1, 10000)
number_2 = random.randint(1, 10000)
print("number_1", number_1, "number_2", number_2)

if number_1 > number_2:
    print("პირველი რიცხვი მეტია")
elif number_2 == number_1:
    print("რიცხვები ტოლია")
else:
    print("მეორეა მეტი")
