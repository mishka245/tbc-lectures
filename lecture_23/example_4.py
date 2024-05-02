try:
    file = open("test.txt", 'w')
except PermissionError:
    print("you don't have permission")