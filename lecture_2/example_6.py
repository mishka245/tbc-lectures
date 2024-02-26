"""
დავწეროთ პროგრამა რომელიც რომელიც
მიიღებს არგუმენტად ტემპერატურას და
ინფორმაციას წვიმაზე(კი ან არა)

პროგრამამ უნდა შემოგვთავაზოს როგორ მოვიქცეთ.
"""

temperature = int(input("What is outside temperature in celsius? "))
is_raining = input("Is it raining? (yes or no)") == "yes"

if is_raining:
    if temperature > 20:
        print("Keep calm and program")
    else:
        print("Stay home and read book")
else:
    if temperature > 20:
        print("Lets go for a hike")
    else:
        print("Go to your favorite coffe shop")



