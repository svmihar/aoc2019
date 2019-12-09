from collections import defaultdict

digits = [int(x) for x in open('input.txt').read().strip()]
layers = int(len(digits)/(25*6))
G = [[' '  for _ in range(25)] for _ in range(6)]
C = defaultdict(lambda:defaultdict(int))
for l in range(layers): 
    for r in range(6): 
        for c in range(25): 
            if digits[l*25*6+r*25+c]==0 and G[r][c] == ' ' : 
                G[r][c] = '.'
            elif digits[l*25*6+r*25+c]==1 and G[r][c] == ' ':  
                G[r][c] = '#'
    for i in range(25*6): 
        C[l][digits[l*25*6+i]] += 1

best = (10000,0)
for l in range(layers): 
    if(C[l][0],l) <= best: 
        best = (C[l][0],l)
l = best[1]
print(C[l][1]*C[l][2])


for r in range(6): 
    for c in range(25): 
        print(G[r][c], end='')
    print()
