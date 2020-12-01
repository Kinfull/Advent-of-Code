
##########part 1############

with open(r"2020\1\1.txt", "r") as f:
    numberList = [int(numbers) for numbers in f.read().splitlines()]

for i in numberList:
    for j in numberList:
        if(i + j == 2020):
            print(i * j)

##########part 2#############
with open(r"2020\1\1.txt", "r") as f:
    numberList = [int(numbers) for numbers in f.read().splitlines()]

for i in numberList:
    for j in numberList:
        for k in numberList:
            if( i + j + k == 2020):
                print(i * j * k)

