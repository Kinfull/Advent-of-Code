with open(r"2020\2\2.txt", "r") as f:
    passwordList = [lines.split(":") for lines in f.readlines()]

#amount of valid passwords
valid_passwords = 0

############part 1################

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

    # if temp_count is within numbersLow an numbersHigh += valid_passwords (password is valid)
    if((temp_count >= int(numbersLow)) and (temp_count <= int(numbersHigh))):
        valid_passwords += 1
print(valid_passwords)

############part 2###############

for passwords in passwordList:
    #temp_count = amount of times rule occurs in password
    temp_count = 0

    #the first index in passwords (the list that contains desired values)
    numbers = passwords[0].split("-")
    
    #numbersLow = lowest number it can contain
    numbersLow = numbers[0]
    
    #numbersHigh = Highest number it can contain
    numbersTemp = numbers[1].split()
    numbersHigh = numbersTemp[0]
    
    #rule = what character it has to contain
    rule = numbersTemp[1]

    #if desired chaacter is at positon numbersLow or position numbersHigh in passwords and numbersLow is not the same as numbersHigh then password is valid
    if(((rule == passwords[1][int(numbersLow)]) or (rule == passwords[1][int(numbersHigh)])) and (passwords[1][int(numbersLow)] != passwords[1][int(numbersHigh)])):
        valid_passwords += 1

print(valid_passwords)