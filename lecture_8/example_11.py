SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

action = input("Encrypt or decrypt (e/d): ")
key = int(input("Please enter key (0, 26): "))
text = input("Please enter text: ")
text = text.upper()  # For simplicity, we work only on uppercase
output_text = ""


for c in text:
    c_index = -1
    for i in range(len(SYMBOLS)):
        if SYMBOLS[i] == c:
            c_index = i
    # Escape non encryptable symbols, for example ` `
    if c_index == -1:
        output_text += c
        continue
    if action == "e":
        output_index = (c_index - key) % len(SYMBOLS)
    elif action == "d":
        output_index = (c_index + key) % len(SYMBOLS)
    else:
        print("Incorrect action")
        exit(1)
    output_text = output_text + SYMBOLS[output_index]

print(output_text)
