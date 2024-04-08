"""
დაწერეთ პროგრამა რომელიც მიიღებს მოთამაშეების რაოდენობას.
Პროგრამამ თითოეული მოთამაშისთვის უნდა დააგენერიროს შემთხვევითი
კამათლების წყვილი და დაბეჭდოს ეკრანზე.
"""
import random

gamers_number = int(input("enter number: "))

for gamer in range(1, gamers_number + 1):
    first_number = random.randint(1, 6)
    second_number = random.randint(1, 6)
    print(first_number, second_number)
