MAX_X = -1
MAX_Y = -1
MAX_Z = -1
OFFSETS = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def get_input():
    cubes_map = {}
    cubes = []

    global MAX_X
    global MAX_Y
    global MAX_Z
    
    f = open('inputs/input.txt', 'r')
    for line in f.readlines():
        line = line.strip()
        line = line.split(',')
        cube = (int(line[0]), int(line[1]), int(line[2]))
        
        MAX_X = max(cube[0], MAX_X)
        MAX_Y = max(cube[1], MAX_Y)
        MAX_Z = max(cube[2], MAX_Z)
        
        cubes_map[cube] = 6
        cubes.append(cube)
    f.close()
    return cubes, cubes_map

def common_faces(c1, c2):
    if c1[0] == c2[0] and c1[1] == c2[1] and abs(c1[2] - c2[2]) == 1:
        return True

    if c1[0] == c2[0] and c1[2] == c2[2] and abs(c1[1] - c2[1]) == 1:
        return True

    if c1[1] == c2[1] and c1[2] == c2[2] and abs(c1[0] - c2[0]) == 1:
        return True
    
    return False

def a(cubes, cubes_map):
    for i in range(len(cubes)):
        for j in range(i + 1, len(cubes)):
            if common_faces(cubes[i], cubes[j]):
                cubes_map[cubes[i]] = max(cubes_map[cubes[i]] - 1, 0)
                cubes_map[cubes[j]] = max(cubes_map[cubes[j]] - 1, 0)

    return sum(cubes_map.values())

def BFS(start, wind_map, cubes_map):
    queue = [start]
    visited = {start}
    while queue:
        cube = queue.pop(0)
        wind_map.add(cube)
        for offset_cube in OFFSETS:
            new_cube = (cube[0] + offset_cube[0], cube[1] + offset_cube[1], cube[2] + offset_cube[2])
            if new_cube not in visited:
                visited.add(new_cube)
                if new_cube[0] >= 0 and new_cube[0] <= MAX_X + 1 and new_cube[1] >= 0 and new_cube[1] <= MAX_Y and \
                    new_cube[2] >= 0 and new_cube[2] <= MAX_Z and new_cube not in cubes_map and new_cube not in wind_map:
                        queue.append(new_cube)

def b(cubes, cubes_map):
    for i in range(len(cubes)):
        for j in range(i + 1, len(cubes)):
            if common_faces(cubes[i], cubes[j]):
                cubes_map[cubes[i]] = max(cubes_map[cubes[i]] - 1, 0)
                cubes_map[cubes[j]] = max(cubes_map[cubes[j]] - 1, 0)
    
    pockets_map = {}
    wind_map = set()
    start = (0, 0, 0)
    BFS(start, wind_map, cubes_map)
    
    for i in range(1, MAX_X + 1):
        for j in range(1, MAX_Y + 1):
            for k in range(1, MAX_Z + 1):
                cube = (i, j, k)
                if cube not in wind_map and cube not in cubes_map:
                    pockets_map[cube] = 6
     
    pockets = list(pockets_map.keys())
    
    for i in range(len(pockets)):
        for j in range(i + 1, len(pockets)):
            if common_faces(pockets[i], pockets[j]):
                pockets_map[pockets[i]] = max(pockets_map[pockets[i]] - 1, 0)
                pockets_map[pockets[j]] = max(pockets_map[pockets[j]] - 1, 0)
    
    return sum(cubes_map.values()) - sum(pockets_map.values())
    
if __name__ == '__main__':
    cubes, cubes_map = get_input()
    print(a(cubes, cubes_map))
    cubes, cubes_map = get_input()
    print(b(cubes, cubes_map))


