data = open("inputs/input.txt").read()
map, password = data.split("\n\n")
map = map.split("\n")

pos = map[0].index(".")
dir = 0
dirs = [1, 1j, -1, -1j]
dirn = [">", "v", "<", "^"]
password = password.replace("R", "\nR\n").replace("L", "\nL\n")

firstx = {}
lastx = {}
firsty = {}
lasty = {}

for y, line in enumerate(map):
    for x, c in enumerate(line):
        if c != " ":
            if y not in firstx:
                firstx[y] = x
            lastx[y] = x
            if x not in firsty:
                firsty[x] = y
            lasty[x] = y


def at(p):
    return map[int(p.imag)][int(p.real)]


def wrapx(p):
    x = int(p.real)
    y = int(p.imag)
    if x > lastx[y]:
        x = firstx[y]
    if x < firstx[y]:
        x = lastx[y]
    return x + y * 1j


def wrapy(p):
    x = int(p.real)
    y = int(p.imag)
    if y > lasty[x]:
        y = firsty[x]
    if y < firsty[x]:
        y = lasty[x]
    return x + y * 1j


def wrapx2(p, d):
    x = int(p.real)
    y = int(p.imag)
    if 0 <= y < 50:
        if x >= 150:
            x = 99
            y = 149 - y
            d = (d + 2) % 4
        elif x < 50:
            x = 0
            y = 149 - y
            d = (d + 2) % 4
    elif 50 <= y < 100:
        if x >= 100:
            x = y + 50
            y = 49
            d = (d + 3) % 4
        elif x < 50:
            x = y - 50
            y = 100
            d = (d + 3) % 4
    elif 100 <= y < 150:
        if x >= 100:
            x = 149
            y = 149 - y
            d = (d + 2) % 4
        elif x < 0:
            x = 50
            y = 149 - y
            d = (d + 2) % 4
    elif 150 <= y < 200:
        if x < 0:
            x = y - 100
            y = 0
            d = (d + 3) % 4
        elif x >= 50:
            x = y - 100
            y = 149
            d = (d + 3) % 4
    return x + y * 1j, d


def wrapy2(p, d):
    x = int(p.real)
    y = int(p.imag)
    if 0 <= x < 50:
        if y < 100:
            y = x + 50
            x = 50
            d = (d + 1) % 4
        elif y >= 200:
            y = 0
            x += 100
    elif 50 <= x < 100:
        if y < 0:
            y = x + 100
            x = 0
            d = (d + 1) % 4
        elif y >= 150:
            y = x + 100
            x = 49
            d = (d + 1) % 4
    elif 100 <= x < 150:
        if y < 0:
            x -= 100
            y = 199
        elif y >= 50:
            y = x - 50
            x = 99
            d = (d + 1) % 4
    return x + y * 1j, d


for c in password[:-1].split("\n"):
    # print(c)
    try:
        dist = int(c)
        for i in range(dist):
            nextpos = pos + dirs[dir]
            if dir % 2 == 0:
                nextpos, nextdir = wrapx2(nextpos, dir)
            else:
                nextpos, nextdir = wrapy2(nextpos, dir)
            if at(nextpos) != "#":
                # print(dirn[dir])
                pos = nextpos
                dir = nextdir
    except ValueError:
        rl = c
        if rl == "R":
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4
        # print("dir", dir)

x = int(pos.real) + 1
y = int(pos.imag) + 1
# print(x, y, dir)
print(y * 1000 + x * 4 + dir)
