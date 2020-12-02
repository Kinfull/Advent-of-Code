with open(r"2020\2\2.txt", "r") as f:
    passwordSet = f.readlines()

passwordDict = dict.fromkeys(passwordSet)

for i in range(len(passwordDict), 4):
    print(i)
    

for i in passwordDict:
    print(f"{i}: {passwordDict[i]}")

print(passwordDict)