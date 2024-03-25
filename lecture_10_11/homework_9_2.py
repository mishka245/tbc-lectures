"""
დაწერეთ პროგრამა რომელიც მიიღებს ორ სტიქონს.
Პროგრამამ უნდა შეამოწმოს არის თუ არა შესაძლებელი ერთი სტრიქოქნის სიმბოლოების გამოყენებით მეორე სტრიქონის მიღება.
მაგალითი 1.
	Input:
	listen
	silent
	Output: YES
მაგალითი 2.
	Input:
	a gentleman
	elegant man
	Output: YES
მაგალითი 3.
	Input:
	dormitory
	dirty room
	Output: NO
მაგალითი 4.
	Input:
	election
	collection
	Output: NO
"""

a = input("Please enter text a: ")
b = input("Please enter text b: ")

if len(a) != len(b):
    print("NO")
    exit(1)

result = "YES"
for c in a:
    count_in_a = a.count(c)
    count_in_b = b.count(c)
    if count_in_a != count_in_b:
        result = "NO"
        break

print(result)
