def solve_part_1(arr):
    return max(sum(e) for e in arr)

def solve_part_2(arr):
    return sum(sorted([sum(e) for e in arr],reverse=True)[:3])

if __name__ == '__main__':
    with open('inputs/input.txt') as f:
        arr = []
        for segment in f.read().split('\n\n'):
            arr.append(list(map(int,segment.split('\n'))))

        print('Part 1:', solve_part_1(arr))
        print('Part 2:', solve_part_2(arr))