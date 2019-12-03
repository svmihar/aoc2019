from day2_1 import opcode, geser, input_data

if __name__ == "__main__":
    for noun, verb in ((a, b) for a in range(100) for b in range(100)):
        ret = opcode(geser(input_data, {1: noun, 2: verb}))

        if ret == 19690720:
            part_two = 100 * noun + verb
            print(part_two)
