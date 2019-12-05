data = ''.join(open('input.txt').read().splitlines())
input_data = [int(i) for i in data.split(',')]

def geser(n, inputan):
    n = n[:]
    for k, v in inputan.items():
        n[k] = v
    return n


def opcode(n):
    n = n[:]
    sabi = 0

    while True:
        command = n[sabi:]
        opc = command[0]

        if opc == 1:
            a, b, c = command[1:4]
            n[c] = n[a]+n[b]
            sabi += 4
        elif opc == 2:
            a, b, c = command[1:4]
            n[c] = n[a]*n[b]
            sabi += 4
        elif opc == 2:
            a = n[sabi+1]
            n[a]
        elif opc == 99:
            return n[0]
        else:
            raise ValueError('opcode lu ngacoo bro')
if __name__ == "__main__":
    part_one = opcode(geser(input_data,{1:12,2:2}) )
    print(part_one)
