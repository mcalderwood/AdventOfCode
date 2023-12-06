with open('/Users/matt/Projects/Advent of Code/2020/aoc-day8-input.txt') as my_file:
    boot_code = my_file.readlines()

pc = 0
acc = 0

while boot_code[pc] != "":
    operation = boot_code[pc]
    boot_code[pc] = ""
    
    opcode = operation[0:3]
    operand = operation[4:]

    if opcode == "acc":
        acc += int(operand)
        #
        #sign = boot_code[4]
        #number = boot_code[5:]
        #if sign == "+":
        #    acc += int(number)
        #elif sign == "-":
        #    acc -= int(number)
        #else:
        #    print("Error!  WTF is " + sign + " doing here")*/
        pc += 1

    elif opcode == "jmp":
        pc += int(operand)

    elif opcode == "nop":
        pc += 1

    else:
        print("Error!  WTF is " + operand)

print(acc)