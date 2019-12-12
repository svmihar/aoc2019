from typing import NamedTuple, List, Tuple
from dataclasses import dataclass
import copy


@dataclass
class position:
    x: int
    y: int
    z: int

    def energy(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)


class Moon():
    def __init__(self, position_: position, velocity: position = None):
        self.posisi = position_
        self.velocity = velocity or position(0, 0, 0)

    def __repr__(self):
        return f'Moon(posisi={self.posisi}, velocity={self.velocity})'

    def pot(self) -> int:
        return self.posisi.energy()

    def kin(self) -> int:
        return self.velocity.energy()

    def total_energy(self) -> int:
        return self.pot() * self.kin()

    def apply_velocity(self) -> None:
        self.posisi.x += self.velocity.x
        self.posisi.y += self.velocity.y
        self.posisi.z += self.velocity.z

    def state_x(self) -> Tuple:
        return (self.posisi.x, self.velocity.x)

    def state_y(self) -> Tuple:
        return (self.posisi.y, self.velocity.y)

    def state_z(self) -> Tuple:
        return (self.posisi.z, self.velocity.z)


def step(moons: List[Moon]) -> None:
    # akselerasi
    for m1 in moons:
        for m2 in moons:
            if m1 != m2:
                # atur akselerasi sesuai aturan
                if m1.posisi.x < m2.posisi.x:
                    m1.velocity.x += 1
                elif m1.posisi.x > m2.posisi.x:
                    m1.velocity.x -= 1

                if m1.posisi.y < m2.posisi.y:
                    m1.velocity.y += 1
                elif m1.posisi.y > m2.posisi.y:
                    m1.velocity.y -= 1

                if m1.posisi.z < m2.posisi.z:
                    m1.velocity.z += 1
                elif m1.posisi.z > m2.posisi.z:
                    m1.velocity.z -= 1
    # apply kecepatan
    for moon in moons:
        moon.apply_velocity()


def state_x(moons) -> Tuple:
    return (moon.state_x() for moon in moons)


def state_y(moons) -> Tuple:
    return (moon.state_y() for moon in moons)


def state_z(moons) -> Tuple:
    return (moon.state_z() for moon in moons)



def find_state_awal(moons: List[Moon], state_fn) -> int:
    m = copy.deepcopy(moons)
    seen = set()
    seen.add(state_fn(m))
    n_steps = 0
    while True:
        n_steps += 1
        step(m)
        s = state_fn(m)
        if s in seen:
            return n_steps
        else:
            seen.add(s)


if __name__ == "__main__":
    MOONS = [
        Moon(position(-1, 0, 2)),
        Moon(position(2, -10, -7)),
        Moon(position(4, -8, 8)),
        Moon(position(3, 5, -1))
    ]
    for n in range(10):
        step(MOONS)
    print(sum([moon.total_energy() for moon in MOONS]))

    MOONS_input = [
        Moon(position(-19, -4, 2)),
        Moon(position(-9, 8, -16)),
        Moon(position(-4, 5, -11)),
        Moon(position(1, 9, -13))
    ]

    for n in range(1000):
        step(MOONS_input)
    print(sum([moon.total_energy() for moon in MOONS_input]))
    print(find_state_awal(MOONS_input, state_x))
    print(find_state_awal(MOONS_input, state_y))
    print(find_state_awal(MOONS_input, state_z))

