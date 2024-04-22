names = ["John", "Jane", "Jack", "Jill"]
grades = [90, 95, 85, 80]

grades_mapping = {}

for i in range(len(names)):
    grades_mapping[names[i]] = grades[i]

print(grades_mapping)
