"""
დაწერეთ პროგრამა რომელიც მიიღებს მოთამაშეების რაოდენობას.
Პროგრამამ თითოეული მოთამაშისთვის უნდა დააგენერიროს შემთხვევითი
კამათლების წყვილი და დაბეჭდოს ეკრანზე.
მაგალითები
input: 2
0 - 1 3
1 - 2 4
"""

# ცუდი ნაწერია
import random

[print(f"{gamer} - {random.randint(1, 6)} {random.randint(1, 6)}") for gamer in range(int(input("Please, enter gamers number: ")))]

