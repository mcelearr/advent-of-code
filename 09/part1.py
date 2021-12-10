import functools

input = open('input.txt', 'r').read().strip()

cave_rows = input.splitlines()

cave_grid = list(map(lambda x: list(x), cave_rows))

low_points = []

for i, row in enumerate(cave_grid):
    for j, point in enumerate(row):
        current = int(point)
        if i > 0:
            up = int(cave_grid[i-1][j])
        else:
            up = 10

        if i < len(cave_grid) - 1:
            down = int(cave_grid[i+1][j])
        else:
            down = 10

        if j > 0:
            left = int(row[j-1])
        else:
            left = 10

        if j < len(row) - 1:
            right = int(row[j+1])
        else:
            right = 10

        if current < up and current < down and current < left and current < right:
            low_points.append(current)

risk_level = functools.reduce(
    lambda acc, point: acc + point + 1, low_points, 0)

print("Result: {}".format(risk_level))
