"""
დაწერეთ პროგრამა რომელიც მიიღებს მოთამაშეების რაოდენობას.
Პროგრამამ თითოეული მოთამაშისთვის უნდა დააგენერიროს შემთხვევითი
კამათლების წყვილი და დაბეჭდოს ეკრანზე.
მაგალითები
input: 2
0 - 1 3
1 - 2 4
"""

# თუ ბეჭდვაში 4 ქულა იწერება, დავწერდი 2
# +1 უსაფრთხო ინფუთი
import random

gamers_number = int(input("Please, enter gamers number: "))

if gamers_number < 0:
    print("Please enter non negative number")
    exit()


for gamer in range(1, gamers_number + 1):
    first_number = random.randint(1, 6)
    second_number = random.randint(1, 6)
    result_str = f"Gamer {gamer}: {first_number}, {second_number}"
    print(result_str)
