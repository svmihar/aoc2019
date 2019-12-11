import math
from collections import defaultdict
from typing import List, Dict, NamedTuple, Tuple, Iterator


class Asteroid(NamedTuple):
    x: int
    y: int


Asteroids = List[Asteroid]


def parse(raw: str) -> Asteroid:
    return [
        Asteroid(x, y)
        for y, line in enumerate(raw.split("\n"))
        for x, c in enumerate(line)
        if c == '#'
    ]


def count_visible(asteroids: Asteroids, station: Asteroid) -> int:
    # recenter all visible asteroids
    slopes = set()
    for x, y in asteroids:
        dx = x - station.x
        dy = y - station.y

        fpb = math.gcd(dx, dy)

        if dx == dy == 0:
            pass
        else:
            slopes.add((dx/fpb, dy/fpb))
    return len(slopes)


def best_station(asteroids: Asteroids) -> tuple((Asteroid, int)):
    results = [(a, count_visible(asteroids, a)) for a in asteroids]
    return max(results, key=lambda pair: pair[1])


# asserting stuff karena harus main aman :)
test_1 = parse('''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####''')
assert best_station(test_1) == Asteroid((5, 8), 33)

test_2 = parse('''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
''')
assert best_station(test_2) == Asteroid((1, 2), 35)

test_3 = parse('''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##''')
assert best_station(test_3) == Asteroid((11, 13), 210)

input_ = open('input.txt').read()
print(best_station(parse(input_)))


def faux_angle(asteroid): 
    dx,dy = asteroid 
    if dx == 0 and dy < 0: 
        return (0,0)
    elif dx > 0 and dy<0: 
        return (1,dx/abs(dy))
    elif dx > 0 and dy == 0: 
        return (2,0)
    elif dx > 0 and dy > 0: 
        return (3, dy/dx) 
    elif dx == 0 and dy > 0: 
        return (4,0)
    elif dx < 0 and dy > 0: 
        return (5, abs(dx)/dy)
    elif dx < 0  and dy == 0: 
        return (6,0)
    elif dx < 0 and dy < 0: 
        return (7, dy/dx)

def iterate(asteroids: Asteroids, station: Asteroid) -> Iterator[Asteroid]: 
    asteroids_by_angle = defaultdict(list)

    for x, y in asteroids: 
        dx = x - station.x 
        dy = y - station.y

        fpb = math.gcd(dx, dy)

        if dx == dy == 0:
            pass
        else:
            angle = (dx / fpb, dy / fpb)
            asteroids_by_angle[angle].append(Asteroid(x,y))
    # sort length descending for each angle
    for angle_asteroids in asteroids_by_angle.values(): 
        angle_asteroids.sort(key=lambda a: abs(a.x - station.x) + abs(a.y - station.y), reverse= True)

    while asteroids_by_angle: 
        keys = asteroids_by_angle.keys() # dx, dy nya 
        keys = sorted(keys, key = faux_angle)

        for key in keys: 
            angle_asteroids = asteroids_by_angle[key] 
            yield angle_asteroids.pop()
            if not angle_asteroids: 
                del asteroids_by_angle[key]



station = best_station(parse(input_))[0]
vaporizations = list(iterate(parse(input_), station))
print(vaporizations[199])
print(vaporizations[199].x * 100 +  vaporizations[199].y)
