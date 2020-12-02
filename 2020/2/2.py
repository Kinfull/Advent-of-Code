with open(r"2020\2\2.txt", "r") as f:
    passwordList = [lines.split(":") for lines in f.readlines()]
count = 0
"""

for passwords in passwordList:
    temp_count = 0
    #temp_count = amount of times rule occurs in password
    numbers = passwords[0].split("-")
    
    numbersLow = numbers[0]
    #numbersLow = lowest number it can contain
    
    numbersTemp = numbers[1].split()
    numbersHigh = numbersTemp[0]
    #numbersHigh = Highest number it can contain
    
    rule = numbersTemp[1]
    #rule = what character it has to contain

    #tests how many times the rule occurs in password (+= temp_count) for evet time it does
    for j in range(len(passwords[1])-1):
        if(rule == passwords[1][j]):
            temp_count += 1

    # if temp_count is within numbersLow an numbersHigh += count (password is valid)
    if((temp_count >= int(numbersLow)) and (temp_count <= int(numbersHigh))):
        count += 1
print(count)
"""

for passwords in passwordList:
    temp_count = 0
    #temp_count = amount of times rule occurs in password
    numbers = passwords[0].split("-")
    
    numbersLow = numbers[0]
    #numbersLow = lowest number it can contain
    
    numbersTemp = numbers[1].split()
    numbersHigh = numbersTemp[0]
    #numbersHigh = Highest number it can contain
    
    rule = numbersTemp[1]
    #rule = what character it has to contain

    if(((rule == passwords[1][int(numbersLow)+1]) or (rule == passwords[1][int(numbersHigh)+1])) and (passwords[1][int(numbersLow)+1] != passwords[1][int(numbersHigh)+1])):
        count += 1

print(count)