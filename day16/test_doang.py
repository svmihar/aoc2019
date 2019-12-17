def berak(n): 
    for _ in range(n): 
        yield 0

    for _ in range(n): 
        yield 1


coba = 7
g = berak(coba) 

for i in range(coba*2): 
    print(next(g))
