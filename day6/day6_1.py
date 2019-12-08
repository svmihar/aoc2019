from typing import NamedTuple, List, Dict, Iterable
from collections import defaultdict


class Node(NamedTuple):
    parent: str
    name: str


def run(s: str) -> int:
    nodes = {'COM': Node('', 'COM')}
    s = open(s).read()
    for line in s.splitlines():
        parent, name = line.split(')')
        nodes[name] = Node(parent, name)
    total = 0
    for node in nodes.values():
        while node.name != 'COM':
            total += 1
            node = nodes[node.parent]
    return total


def parse_input(inputs: Iterable[str]) -> Dict[str, List[str]]:
    planets: Dict[str, List[str]] = defaultdict(list)
    for l  in inputs:
        planet, _, orbiter = l.partition(')')
        planets[orbiter].append(planet)
    return planets

def map_flatter(starmap: Dict[str, List[str]]) -> Dict[str, List[str]]:
    def flat_map(start: str) -> List[str]:
        if start not in starmap:
            return []
        stars = [s for star in starmap[start] for s in flat_map(star)]
        return starmap[start]+stars
    return{star:flat_map(star) for star in starmap}



if __name__ == "__main__":
    total = run('input.txt')
    print(total)
    with open('input.txt') as f:
        data= map(str.strip, f.readlines())

    print(data)
    flat_orbiters = map_flatter(data)
    print(len(set(flat_orbiters['YOU']) ^ set(flat_orbiters['SAN'])))
