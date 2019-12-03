data = open('input_2.txt').read().splitlines()
total = 0

def nilai_fuel(n):
    return max(n//3-2,0)

for mass in data:
    sblm = int(mass)
    while sblm>0:
        sblm = nilai_fuel(sblm)
        print(sblm)
        total+=sblm
print(total)