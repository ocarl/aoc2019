import math
from collections import defaultdict, OrderedDict


class Asteroid:

    all_asts = []
    max_x = 0
    max_y = 0

    best_pos = None
    max_seen = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Asteroid.all_asts.append(self)
        self.can_see = defaultdict(list)
        Asteroid.max_x = max(Asteroid.max_x, x)
        Asteroid.max_y = max(Asteroid.max_y, y)

    def __repr__(self):
        return f'{self.x}, {self.y}'

    def get_neighbors(self):
        asteroids = Asteroid.all_asts.copy()
        asteroids.remove(self)
        for neighbor in asteroids:
            angle = math.atan2((neighbor.y - self.y), (neighbor.x - self.x))
            self.can_see[str(angle)].append(neighbor)

        if len(self.can_see) >= Asteroid.max_seen:
            Asteroid.best_pos = self
            Asteroid.max_seen = len(self.can_see)


def find_loc(ast_map):
    for j, line in enumerate(ast_map.split('\n')):
        for i, point in enumerate(line):
            if point == '#':
                Asteroid(i, j)
    for asteroid in Asteroid.all_asts:
        asteroid.get_neighbors()
    return repr(Asteroid.best_pos), Asteroid.max_seen


def destroy():
    last_one = None
    i = 0
    while len(Asteroid.best_pos.can_see) > 0:
        i += 1
        od = OrderedDict(sorted(Asteroid.best_pos.can_see.items()))
        for k, v in od.items():
            last_one = v
            closest = None
            closest_len = 9999
            for a in v:
                if not closest:
                    closest = a
                    closest_len = math.sqrt((closest.y - Asteroid.best_pos.y)**2 + (closest.x - Asteroid.best_pos.x)**2)
                    continue
                curr_len = math.sqrt((a.y - Asteroid.best_pos.y)**2 + (a.x - Asteroid.best_pos.x)**2)
                if curr_len < closest_len:
                    closest = a
                    closest_len = curr_len
            if v == []:
                Asteroid.best_pos.can_see.pop(k)
        if i == 200:
            break
    return repr(last_one)



ast_map=""".#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##"""

find_loc(ast_map)

print(destroy())

ast_map = """.#..##.###...#######
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
###.##.####.##.#..##"""

Asteroid.all_asts = []
Asteroid.max_x = 0
Asteroid.max_y = 0

Asteroid.best_pos = None
Asteroid.max_seen = 0
find_loc(ast_map)

print(destroy())

with open('input10.txt') as f:
    Asteroid.all_asts = []
    Asteroid.max_x = 0
    Asteroid.max_y = 0

    Asteroid.best_pos = None
    Asteroid.max_seen = 0
    ast_map = f.read()
    print(find_loc(ast_map))
    #poses = [(a.x, a.y) for a in Asteroid.best_pos.can_see]
    #out = ''
    #for j in range(Asteroid.max_y + 1):
    #    for i in range(Asteroid.max_x + 1):
    #        if (i,j) == (Asteroid.best_pos.x, Asteroid.best_pos.y):
    #            out += '#'
    #        elif (i, j) in poses:
    #            out += 'o'
    #        else:
    #            out += '.'
    #    out += '\n'
    #print(out)
