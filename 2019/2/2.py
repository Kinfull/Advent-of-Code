
#########part 1############
if __name__ == "__main__":
    with open(r"2019\2\2.txt", "r") as f:
        instructions = [int(opcodes) for opcodes in f.read().split(",")]

    instructions[1] = 12
    instructions[2] = 2

    for i in range(0, len(instructions), 4):
        if(instructions[i] == 1):
            instructions[instructions[i + 3]] = instructions[instructions[i + 1]] + instructions[instructions[i + 2]]

        elif(instructions[i] == 2):
            instructions[instructions[i + 3]] = instructions[instructions[i + 1]] * instructions[instructions[i + 2]]

        elif(instructions[i] == 99):
            print(instructions[0])

#############part 2#############
with open(r"2019\2\2.txt", "r") as f:
    instructions = [int(opcodes) for opcodes in f.read().split(",")]

def input_proceger(input_array):
    
    array = input_array[:]

    for op in range(0, len(instructions), 4):
        if(array[op] == 1):
            array[array[op+3]] = array[array[op+1]] + array[array[op+2]]

        elif(array[op] == 2):
            array[array[op+3]] = array[array[op+1]] * array[array[op+2]]

        elif(array[op] == 99):
            return array[0]

for noun in range(100):
    for verb in range(100):
        instructions[1] = noun
        instructions[2] = verb
        output = input_proceger(instructions)
        if(output == 19690720):
            print(100 * noun + verb)
            break