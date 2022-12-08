if __name__ == "__main__":
    with open("inputs/input.txt") as file:
        data = file.read().strip().splitlines()
        height = len(data)
        width = len(data[0])
        visible = set()
        scenic = 0

        for y in range(height):
            for x in range(width):
                score = 1
                tree = data[y][x]
                left = data[y][:x][::-1]
                right = data[y][x+1:width]
                up = [data[ny][x] for ny in reversed(range(y))]
                down = [data[ny][x] for ny in range(y+1,height)]
                
                for direction in left, down, up, right:
                    for i, neighbour in enumerate(direction):
                        if tree <= neighbour:
                            score *= i+1; break
                    else:
                        score *= len(direction)
                        visible.add((y,x))
                scenic = max(scenic, score)

        print(len(visible), scenic)