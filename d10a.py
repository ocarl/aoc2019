


class Asteroid:

    all_asts = []
    max_x = 0
    max_y = 0

    def __init__(self, x, y):
        self.coords = [x, y]
        Asteroid.all_asts.append(self)
        self.can_see = []
        Asteroid.max_x = max(Asteroid.max_x, x)
        Asteroid.max_y = max(Asteroid.max_y, y)


    def __repr__(self):
        return ','.join(self.coords)


    def get_neighbors(self, n):
        for perimeter in range(n+1):
            for dist in range(-perimeter, perimeter + 1):
                while True:
                    point = [self.coords[0] + dist






def find_loc(ast_map):
    for j, line in enumerate(ast_map.split('\n')):
        for i, point in enumerate(line):
            if point == '#':
                Asteroid(i, j)
    for asteroid in Asteroid.all_asts:
        perimeter =






ast_map = """.#..#
.....
#####
....#
...##"""

assert find_loc(ast_map) == (3,4)