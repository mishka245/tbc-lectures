# for i in range(20):
#     if i % 3 != 0:
#         print(i)

for i in range(20):
    if i % 3 == 0:
        continue
    if i % 7 == 0:
        continue
    print(i)

# for i in range(20):
#     if i % 3 == 0 or i % 7 == 0:
#         continue
#     print(i)


print("Finished")
