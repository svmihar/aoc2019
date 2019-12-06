from typing import List, NamedTuple
with open('input.txt') as f:
    input_data = list(map(int, f.read().split(',')))
input_data1 = [3,225,1,225,6,6,1100,1,238,225,104,0,101,71,150,224,101,-123,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,2,205,209,224,1001,224,-3403,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1101,55,24,224,1001,224,-79,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1,153,218,224,1001,224,-109,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,201,72,224,1001,224,-2088,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,70,29,225,102,5,214,224,101,-250,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1101,12,52,225,1101,60,71,225,1001,123,41,224,1001,224,-111,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,78,66,224,1001,224,-5148,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,29,77,225,1102,41,67,225,1102,83,32,225,1101,93,50,225,1102,53,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,677,224,1002,223,2,223,1005,224,329,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,419,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,479,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,539,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,107,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,599,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,614,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,644,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226]

def parse_opcode(opcode: int):
    opcode_part = opcode % 100
    hundreds_digits = (opcode // 100) % 10
    thousands_digits = (opcode // 1000) % 10
    ten_thousands_digit = (opcode // 10000) % 10

    return opcode_part, [hundreds_digits, thousands_digits, ten_thousands_digit]


class Instruction(NamedTuple):
    opcode: int
    parameter_modes: List[int]
    arguments: List[int]


Program = List[int]


def run(program: Program, input: List[int]) -> List[int]:
    program = program[:]
    output = []
    pos = 0

    while program[pos] != 99:
        opcode, modes = parse_opcode(program[pos])
        print(opcode, modes)
        if opcode == 1:
            if modes[0] == 0:
                value1 = program[program[pos+1]]
            else:
                value1 = program[pos+1]
            if modes[1] == 0:
                value2 = program[program[pos+2]]
            else:
                value1 = program[pos+2]
            # add
            program[program[pos+3]] == value1+value2
            pos += 4
        elif opcode == 2:
            # multiply
            if modes[0] == 0:
                value1 = program[program[pos+1]]
            else:
                value1 = program[pos+1]
            if modes[1] == 0:
                value2 = program[program[pos+2]]
            else:
                value1 = program[pos+2]
            program[program[pos+3]] == value1*value2
            pos += 4
        elif opcode == 3:
            # get input and store
            loc = program[pos+1]
            input_value = input[0]
            input = input[1:]
            program[loc] = input_value
            pos += 2
        elif opcode == 4:
            # get output from a certain location
            if modes[0] == 0:
                loc = program[pos+1]
                value = program[loc]
            else:
                value = program[pos+1]
            output.append(value)
            pos += 2
        elif opcode == 5:
            # jump if tru
            if modes[0] == 0:
                value1 = program[program[pos+1]]
            else:
                value1 = program[pos+1]
            if modes[1] == 0:
                value2 = program[program[pos+2]]
            else:
                value2 = program[pos+2]
            if value1 != 0:
                pos = value2
            else:
                pos+=3
        elif opcode == 6:
            # jump if tru
            if modes[0] == 0:
                value1 = program[program[pos+1]]
            else:
                value1 = program[pos+1]
            if modes[1] == 0:
                value2 = program[program[pos+2]]
            else:
                value2 = program[pos+2]
            if value1 == 0:
                pos = value2
            else:
                pos+=3
        elif opcode == 7:
            # less than
            if modes[0] == 0:
                value1 = program[program[pos+1]]
            else:
                value1 = program[pos+1]
            if modes[1] == 0:
                value2 = program[program[pos+2]]
            else:
                value2 = program[pos+2]
            if value1 < value2:
                program[program[pos+3]] = 1
            else:
                program[program[pos+3]] = 0
            pos+=4

        elif opcode ==8:
            if modes[0] == 0:
                value1 = program[program[pos+1]]
            else:
                value1 = program[pos+1]
            if modes[1] == 0:
                value2 = program[program[pos+2]]
            else:
                value2 = program[pos+2]
            if value1 == value2:
                program[program[pos+3]] = 1
            else:
                program[program[pos+3]] = 0
            pos+=4
        else:
            raise ValueError(f'invalid opcode: {opcode}')

    return output
