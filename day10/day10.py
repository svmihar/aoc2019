import math
from typing import List, Dict, NamedTuple, Tuple


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
