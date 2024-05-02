
try:
    file = open("hi.txt", "r")
    file_content = file.read()
    print(file_content)
    file.close()
except:
    print("Can't open file")

