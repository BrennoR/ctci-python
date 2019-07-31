# Draw Line


def draw_line(screen, width, x1, x2, y):
    if x1 == x2:
        screen[y][x1 // 8][0] |= 1 << (7 - (x1 % 8))

    if x2 - x1 >= 8:
        start_mask = (1 << (8 - (x1 % 8))) - 1
    else:
        mid_mask = ((1 << (x2 - x1)) - 1) << (7 - (x2 % 8))
        screen[y][x1 // 8][0] |= mid_mask
        return screen

    screen[y][x1 // 8][0] |= start_mask
    start_idx = (x1 + (8 - (x1 % 8))) // 8
    end_idx = (x2 - (x2 % 8)) // 8
    for x in range(start_idx, end_idx):
        mask = (1 << 8) - 1
        screen[y][x][0] |= mask

    end_mask = ((-1 << (7 - (x2 % 8))) % (1 << 8))
    screen[y][x2 // 8][0] |= end_mask
    return screen


if __name__ == '__main__':
    screen = [[[0b10110011], [0b10011001], [0b10010010], [0b10000000]],
              [[0b11001100], [0b00110000], [0b10111110], [0b11100000]],
              [[0b10011010], [0b10101111], [0b00101111], [0b10100101]],
              [[0b10100000], [0b11001100], [0b01011001], [0b00111011]],
              [[0b10111101], [0b01101011], [0b01101101], [0b11111000]]]

    screen = draw_line(screen, 10, 10, 31, 2)

    for r in screen:
        for c in r:
            for byte in c:
                print(bin(byte), end='\t')
        print()




