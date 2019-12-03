import math

data = open('input.txt').read().splitlines()
total = 0
for mass in data:
    total+=int(mass)//3-2
    if mass == 12:
        fuel_required= math.floor(mass/3) -2
        assert fuel_required==2,'fuel is not met by requirement#1'
    elif mass == 14:
        fuel_required = math.floor(mass/3) - 2
        assert fuel_required==2,'fuel is not met by requirement#2'
    elif mass == 1969:
        pass

print(total)
