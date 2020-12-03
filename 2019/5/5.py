with open(r"2019\5\5.txt", "r") as f:
    instructions = [int(opcodes) for opcodes in f.read().split(",")]




for opcode in range(len(instructions)):

    op = instructions[opcode]

    if len(op) > 1:
        pass
    else:
        if op == 3:
            user_input = int(input("Enter input: "))
            instructions[int(op)] = user_input
        if op == 4:
            print(instructions[int(op)])
    