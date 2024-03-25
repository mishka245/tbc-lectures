# search for substring 'bob'
s = "azcbobobegghakl"
#    0123
count = 0
for i in range(0, len(s) - 3):
    if s[i:i + 3] == "bob":
        count += 1
print("'bob' count is - ", count)
