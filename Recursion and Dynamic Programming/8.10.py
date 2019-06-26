# Paint Fill


def paint_fill_helper(point, ocolor, ncolor, screen):
    i, j = point
    if i < 0 or i >= len(screen) or j < 0 or j >= len(screen[0]):
        return

    if screen[i][j] == ocolor:
        screen[i][j] = ncolor
        paint_fill_helper([i + 1, j], ocolor, ncolor, screen)
        paint_fill_helper([i - 1, j], ocolor, ncolor, screen)
        paint_fill_helper([i, j + 1], ocolor, ncolor, screen)
        paint_fill_helper([i, j - 1], ocolor, ncolor, screen)


def paint_fill(point, ncolor, screen):
    i, j = point
    ocolor = screen[i][j]
    return paint_fill_helper(point, ocolor, ncolor, screen)


if __name__ == '__main__':
    screen_1 = [['B', 'C', 'G', 'G', 'R', 'R', 'T'],
                ['B', 'T', 'G', 'G', 'R', 'P', 'T'],
                ['B', 'C', 'G', 'G', 'R', 'R', 'T'],
                ['G', 'R', 'G', 'G', 'R', 'K', 'T'],
                ['B', 'C', 'B', 'G', 'R', 'R', 'T'],
                ['B', 'R', 'G', 'R', 'R', 'R', 'T'],
                ['P', 'C', 'G', 'G', 'B', 'R', 'G']]

    paint_fill([3, 3], 'B', screen_1)
    print(screen_1)
