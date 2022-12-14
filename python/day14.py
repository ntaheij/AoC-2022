range_sorted = lambda *p: range(min(p), max(p)+1)
blocked = set()

if __name__ == "__main__":
    input = open('inputs/input.txt')
    for ps in [[[*map(int, c.split(','))] for c in l.split('->')] for l in input]:
        for (x1, y1), (x2, y2) in zip(ps, ps[1:]):
            blocked |= {complex(x, y) for x in range_sorted(x1, x2)
                                    for y in range_sorted(y1, y2)}

    floor = max(p.imag for p in blocked)
    part1, rock = 0, len(blocked)

    while 500 not in blocked: 
        pos = 500
        while True:
            if pos.imag > floor:
                if not part1: part1 = len(blocked)
                break
            for dest in pos+1j, pos-1+1j, pos+1+1j:
                if dest not in blocked:
                    pos = dest
                    break
            else: break
        blocked.add(pos)

    print(part1-rock, len(blocked)-rock)