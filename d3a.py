class Wire:
    def __init__(self, inputs):
        self.inputs = inputs.split(',')
        self.locations = [(0, 0)]
        self.walk_self()

    def walk_self(self):
        for direction in self.inputs:
            current_pos = self.locations[-1]
            if 'R' in direction:
                for i in range(int(direction.replace('R',''))):
                    self.locations.append(
                        (current_pos[0] + i + 1, current_pos[1]))
            if 'L' in direction:
                for i in range(int(direction.replace('L',''))):
                    self.locations.append(
                        (current_pos[0] - i - 1, current_pos[1]))
            if 'U' in direction:
                for i in range(int(direction.replace('U',''))):
                    self.locations.append(
                        (current_pos[0], current_pos[1] + i + 1))
            if 'D' in direction:
                for i in range(int(direction.replace('D',''))):
                    self.locations.append(
                        (current_pos[0], current_pos[1] - i - 1))


def check_wires(string_array):
    import math
    wire1 = Wire(string_array[0])
    wire2 = Wire(string_array[1])

    print('wires')

    crossings = []

    for loc1 in wire1.locations:
        for loc2 in wire2.locations:
            if loc2 != (0, 0) and loc1 == loc2:
                crossings.append(loc2)

    print(crossings)

    cross_dists = []
    for cross in crossings:
        cross_dists.append(sum((math.sqrt(cross[0]**2), math.sqrt(cross[1]**2))))

    print(cross_dists)

    return min(cross_dists)


assert check_wires(['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83']) == 159

with open('input3.txt') as f:
    print(check_wires(f.readlines()))
