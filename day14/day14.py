from copy import deepcopy


def p1(s):
    n, item = s.split()
    return int(n), item


OIN = {}
F = {}
for line in open("input.txt").readlines():
    line = line.strip()
    need, get = line.split(" => ")
    n_get, get = p1(get)
    need = need.split(", ")
    need = [p1(s.strip()) for s in need]
    for (n, y) in need:
        if y not in OIN:
            OIN[y] = 0
        OIN[y] += 1
    assert get not in F
    F[get] = (n_get, need)


def cost(nfuel):
    IN = deepcopy(OIN)
    IN['FUEL'] = 0
    REQ = {'FUEL': nfuel}
    done = False

    while not done:
        for x in IN:
            if IN[x] == 0:
                n = REQ[x]
                print(x, n)
                if x == 'ORE':
                    return n
                (n_get, need) = F[x]
                amt = (n+n_get-1)//n_get
                for (ny, y) in need:
                    if y not in REQ:
                        REQ[y] = 0
                    REQ[y] += amt*ny
                    IN[y] -= 1
                del IN[x]
                break


lo = 0
hi = 1e12
while lo < hi:
    mid = (lo+hi+2)//2
    if cost(mid) <= int(1e12):
        lo = mid
    else:
        hi = mid-1
print(lo)
