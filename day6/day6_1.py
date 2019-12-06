from typing import NamedTuple

class Node(NamedTuple):
    parent: str
    name: str

def run(s: str) -> int:
    nodes = {'COM': Node('','COM')}
    s = open(s).read()
    for line in s.splitlines():
        parent, name = line.split(')')
        nodes[name] = Node(parent,name)
    total = 0
    for node in nodes.values():
        while node.name != 'COM':
            total+=1
            node = nodes[node.parent]
    return total

if __name__ == "__main__":
    total = run('input.txt')
    print(total)

