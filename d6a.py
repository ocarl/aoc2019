class Node:

    nodes = []
    orbits = 0
    root = None

    def __init__(self, name):
        self.parent = None
        self.name = name
        self.children = []
        Node.nodes.append(self)

    @staticmethod
    def calc_orbits():
        local_nodes = Node.nodes.copy()
        while local_nodes:
            for node in local_nodes:
                if not node.children:
                    parent = node.parent
                    if parent:
                        parent.children.remove(node)
                    else:
                        Node.root = node
                    local_nodes.remove(node)
                    while parent:
                        Node.orbits += 1
                        node = parent
                        parent = node.parent
        return Node.orbits

    @staticmethod
    def create_tree(in_string):
        for line in in_string.split('\n'):
            parent_name, child_name = line.split(')')
            parent = Node.node_factory(parent_name)
            child = Node.node_factory(child_name)
            child.parent = parent
            parent.children.append(child)

    @staticmethod
    def node_factory(name):
        for x in Node.nodes:
            if name == x.name:
                return x
        return Node(name)

    @staticmethod
    def clear():
        Node.nodes = []
        Node.orbits = 0
        Node.root = None


test_in = """CAM)B
D)E
E)F
B)G
G)H
D)I
E)J
B)C
C)D
J)K
K)L"""

Node.create_tree(test_in)
assert Node.calc_orbits() == 42
Node.clear()

test_in = """CBM)B
D)E
E)F
B)G
G)H
D)I
E)J
B)C
J)M
J)N
M)O
C)D
J)K
K)L"""

Node.create_tree(test_in)
print(Node.calc_orbits())
Node.clear()

with open('input6.txt') as f:
    Node.create_tree(f.read())
    res = Node.calc_orbits()
    print(res)


