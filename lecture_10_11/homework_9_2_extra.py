from collections import Counter

print("YES") if Counter(input("Please enter text a: ")) == Counter(input("Please enter text b: ")) else print("NO")
