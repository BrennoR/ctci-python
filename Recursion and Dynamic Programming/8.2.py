# Robot in a Grid


# TODO: Fix algorithm
# Works but not exactly best path nor efficient
def grid_recurse(grid, i, j, path, memo):
    if grid[i][j] != 1:
        path.append([i, j])
        memo.add((i, j))
        if 0 <= j < (len(grid[0]) - 1) and (i, j + 1) not in memo:
            right = grid_recurse(grid, i, j + 1, path, memo)
            if right and grid[right[-1][0]][right[-1][1]] == 2:
                return right
        if 0 <= i < (len(grid) - 1) and (i + 1, j) not in memo:
            down = grid_recurse(grid, i + 1, j, path, memo)
            if down and grid[down[-1][0]][down[-1][1]] == 2:
                return down
        return path


def robot_in_grid(grid):
    return grid_recurse(grid, 0, 0, [], set())


grid_1 = [[0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 2]]

grid_2 = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 2]]


print(robot_in_grid(grid_1))
print(robot_in_grid(grid_2))
