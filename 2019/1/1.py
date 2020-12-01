
##########part 1############
"""
with open(r"2019\1\1.txt", "r") as f:
    numberList = [int(numbers) for numbers in f.read().splitlines()]

formula = 0

for i in numberList:
    formula += i//3-2

print(formula)
"""

#########part 2############

with open(r"2019\1\1.txt", "r") as f:
    numberList = [int(numbers) for numbers in f.read().splitlines()]

formula = 0

for i in numberList:
    tempFuel = i//3-2
    formula += tempFuel
    while((tempFuel//3)-2 > 0):
        tempFuel = (tempFuel//3)-2
        formula += tempFuel
print(formula)