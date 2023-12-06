with open('/Users/matt/Projects/Advent of Code/2020/aoc-day8-input.txt') as my_file:
    boot_code = my_file.readlines()

pc = 0
acc = 0
possible_changes = []

orig_boot_code = boot_code.copy()

while boot_code[pc] != "":

    operation = boot_code[pc]
    boot_code[pc] = ""
    
    opcode = operation[0:3]
    operand = operation[4:]

    if opcode == "acc":
        acc += int(operand)
        pc += 1

    elif opcode == "jmp":
        possible_changes.append(pc)
        pc += int(operand)

    elif opcode == "nop":
        possible_changes.append(pc)
        pc += 1

    else:
        print("Error!  WTF is " + opcode)

    if pc == len(boot_code):
        print("YAY")
        break

found = False
while True:
    boot_code = orig_boot_code.copy()
    pc = 0
    acc = 0
    
    # Get line to change
    line_to_change = possible_changes.pop()

    if boot_code[line_to_change][0:3] == "jmp":
        boot_code[line_to_change] = "nop" + boot_code[line_to_change][3:]
    elif boot_code[line_to_change][0:3] == "nop":
        boot_code[line_to_change] = "jmp" + boot_code[line_to_change][3:]
    else:
        print("Error!  WTF is " + boot_code[line_to_change])
    
    while boot_code[pc] != "":

        operation = boot_code[pc]
        boot_code[pc] = ""
        
        opcode = operation[0:3]
        operand = operation[4:]

        if opcode == "acc":
            acc += int(operand)
            pc += 1

        elif opcode == "jmp":
            pc += int(operand)

        elif opcode == "nop":
            pc += 1

        else:
            print("Error!  WTF is " + opcode)

        if pc == len(boot_code):
            print("YAY")
            print(acc)
            found = True
            break

    if found:
        break