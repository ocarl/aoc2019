class Node:

    nodes = []
    orbits = 0
    root = None

    def __init__(self, name):
        self.parent = None
        self.name = name
        self.children = []
        Node.nodes.append(self)

    def __repr__(self):
        return self.name + ': ' + ' '.join([x.name for x in self.children])

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
    def calc_distance(start, end):
        start = Node.node_factory(start)
        you = Node.node_factory('YOU')
        you._pivot()
        end = Node.node_factory(end)
        return start._look_for(end, 0)

    def _look_for(self, node, counter):
        if node in self.children:
            return counter
        else:
            for child in self.children:
                counter = child._look_for(node, counter)
                counter += 1
        return counter


    def _pivot(self):
        Node.root = self
        prev = self
        self.children.append(self.parent)
        current = self.parent
        while current != None:
            current.children.remove(prev)
            current.children.append(current.parent)
            mem = current.parent
            current.parent = prev
            prev = current
            current = mem
        self.parent = None



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


test_in = """COM)B
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)YOU
I)SAN
B)C
M)O
C)D
K)L"""

Node.create_tree(test_in)
print(Node.calc_distance('D', 'SAN'))
Node.clear()

with open('input6.txt') as f:
    Node.create_tree(f.read())
    res = Node.calc_orbits()
    print(res)


