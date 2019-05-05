# Robot in a Grid


# TODO: Fix algorithm
def grid_recurse(grid, i, j, path):
    path.append([i, j])
    if grid[i][j] == 2:
        return path
    if 0 <= i < (len(grid) - 1) and grid[i + 1][j] != 1:
        down_path = grid_recurse(grid, i + 1, j, path)
        if down_path:
            return down_path
    if 0 <= j < (len(grid[0]) - 1) and grid[i][j + 1] != 1:
        right_path = grid_recurse(grid, i, j + 1, path)
        if right_path:
            return right_path


def robot_in_grid(grid):
    return grid_recurse(grid, 0, 0, [])


grid_1 = [[0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 2]]

grid_2 = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 2]]


print(robot_in_grid(grid_1))
print(robot_in_grid(grid_2))
