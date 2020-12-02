with open(r"viggo.txt", "r") as f:
    lista = f.read()

count = 0
for i in lista:
    if i == "n":
        count -= 1
    elif i == "u":
        count += 1

print(count)

