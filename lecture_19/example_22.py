"""
წიგნი - 25 -- განათლება
ჩოგბურთის გურთი - 104 -- გართობა
ჭვერის შამპუნი - 28 -- ჰიგიენა
კურსი უდემიზე - 28 განათლება

---
განათლება 25
ჰიგიენა 25
გართობა 104
განთლება 25
ჰიგიენა 55
გართობა 43
ტრანსპორტი 5
finish!
"""
FINISH_KEYWORD = "finish!"


categories = {}

while True:
    user_input = input("Enter expense:")
    if user_input.lower() == FINISH_KEYWORD:
        break

    category, amount = user_input.split(" ")
    if category in categories:
        categories[category] += int(amount)
    else:
        categories[category] = int(amount)


for category, amount in categories.items():
    print(category, "-", amount)
