s = "Hello"

print(s[2])
# s[2] = "@"  # Does not work
s = s[:2] + "@" + s[3:]
print(s)



