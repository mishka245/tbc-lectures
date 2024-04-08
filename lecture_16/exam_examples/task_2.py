"""
დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1.
პროგრამამ უნდა დაითვალის რიცხვი x და დაბეჭდოს ეკრანზე.
Რიცხვი x ის დათვლის პრინციპი ასეთია.
x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1) )

"""

n = int(input("Enter n :"))

if n <= 1:
    print("Please enter n, n > 1")
else:
    s = 1
    i = 3
    sign = -1
    while i <= (2 * n) - 1:
        s = s + sign * (1 / i)
        sign = sign * -1
        i += 2
    result = 4 * s
    print("Result:", result)
