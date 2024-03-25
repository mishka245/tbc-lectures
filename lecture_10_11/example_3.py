s = "azcbobobegghakl"
#    01234

max_substring = ""

substring_index = 0
substring = s[0]  # "a"

for i in range(1, len(s)):
    if substring[-1] <= s[i]:
        substring += s[i]
    else:
        if len(substring) > len(max_substring):
            max_substring = substring
        substring_index = i
        substring = s[i]

print(max_substring)


