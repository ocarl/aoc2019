import math
from collections import defaultdict

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
        #for k, v in self.can_see:
        #    if len(v) > 1:
        #        min_len = 999
        #        for ast in v:
        #            curr_len = math.sqrt(())


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
    #    poses = [(a.x, a.y) for a in asteroid.can_see]
    #    out = ''
    #    for j in range(Asteroid.max_y + 1):
    #        for i in range(Asteroid.max_x + 1):
    #            if (i,j) == (asteroid.x, asteroid.y):
    #                out += '#'
    #            elif (i, j) in poses:
    #                out += 'o'
    #            else:
    #                out += '.'
    #        out += '\n'
    #    print(out)
    return repr(Asteroid.best_pos), Asteroid.max_seen

#ast_map = """.#..#
#.....
######
#....#
#...##"""
#
#assert find_loc(ast_map)[0] == '3, 4'
#Asteroid.all_asts = []
#Asteroid.max_x = 0
#Asteroid.max_y = 0
#
#Asteroid.best_pos = None
#Asteroid.max_seen = 0
#ast_map = """......#.#.
##..#.#....
#..#######.
#.#.#.###..
#.#..#.....
#..#....#.#
##..#....#.
#.##.#..###
###...#..#.
#.#....####"""
#
#assert find_loc(ast_map) == ('5, 8', 33)
#Asteroid.all_asts = []
#Asteroid.max_x = 0
#Asteroid.max_y = 0
#
#Asteroid.best_pos = None
#Asteroid.max_seen = 0
#ast_map = """#.#...#.#.
#.###....#.
#.#....#...
###.#.#.#.#
#....#.#.#.
#.##..###.#
#..#...##..
#..##....##
#......#...
#.####.###."""
#
#assert find_loc(ast_map) == ('1, 2', 35)
Asteroid.all_asts = []
Asteroid.max_x = 0
Asteroid.max_y = 0

Asteroid.best_pos = None
Asteroid.max_seen = 0
ast_map = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""

assert find_loc(ast_map) == ('6, 3', 41)
Asteroid.all_asts = []
Asteroid.max_x = 0
Asteroid.max_y = 0

Asteroid.best_pos = None
Asteroid.max_seen = 0
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

assert find_loc(ast_map) == ('11, 13', 210)

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
