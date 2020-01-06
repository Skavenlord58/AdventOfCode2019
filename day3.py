import argparse as ar
import numpy
from PIL import Image
import timeit


def load_moves_list(input_file) -> list:
    with open(input_file) as f:
        return f.readlines()


def moves_into_moveset(input_str) -> list:
    return input_str.split(',')


def draw_grid():
    # find_intersections()
    indices_x, indices_y = numpy.nonzero(grid)
    return Image.fromarray(grid[indices_x.min():(indices_x.max() + 1), indices_y.min():(indices_y.max() + 1)]
                           .astype(numpy.uint8) * 64)


def moveset_into_instructions(wire: int, moveset):
    wire_pos_x = grid_center_x
    wire_pos_y = grid_center_y
    for f in moveset:
        if f[0] == 'L':
            for a in range(0, int(f[1:])):
                if grid[wire_pos_x][wire_pos_y] < (1 + wire):
                    grid[wire_pos_x][wire_pos_y] += 1 + wire
                wire_pos_y -= 1
        elif f[0] == 'R':
            for a in range(0, int(f[1:])):
                if grid[wire_pos_x][wire_pos_y] < (1 + wire):
                    grid[wire_pos_x][wire_pos_y] += 1 + wire
                wire_pos_y += 1
        elif f[0] == 'U':
            for a in range(0, int(f[1:])):
                if grid[wire_pos_x][wire_pos_y] < (1 + wire):
                    grid[wire_pos_x][wire_pos_y] += 1 + wire
                wire_pos_x -= 1
        elif f[0] == 'D':
            for a in range(0, int(f[1:])):
                if grid[wire_pos_x][wire_pos_y] < (1 + wire):
                    grid[wire_pos_x][wire_pos_y] += 1 + wire
                wire_pos_x += 1
    grid[grid_center_x][grid_center_y] = 0


def find_distances():
    dist = 99999
    for x, y in zip(*numpy.nonzero(grid == 3)):
        new_dist = abs(grid_center_x - x) + abs(grid_center_y - y)
        if new_dist < dist:
            dist = new_dist

    print(f'Part 1 answer: {dist}')


def find_intersections():
    for x in range(0, grid_width):
        for y in range(0, grid_height):
            if grid[x][y] > 2:
                grid[x][y] = 3
            else:
                grid[x][y] = 0


def advance_wires(c, d, wire_one, wire_two):
    while not zip(*numpy.nonzero(grid == 3)):
        wire_pos_x = grid_center_x
        wire_pos_y = grid_center_y
        for f in wire_one:
            c += 1
            if f[0] == 'L':
                for a in range(0, int(f[1:])):
                    if grid[wire_pos_x][wire_pos_y] < 2:
                        grid[wire_pos_x][wire_pos_y] += 2
                    wire_pos_y -= 1
            elif f[0] == 'R':
                for a in range(0, int(f[1:])):
                    if grid[wire_pos_x][wire_pos_y] < 2:
                        grid[wire_pos_x][wire_pos_y] += 2
                    wire_pos_y += 1
            elif f[0] == 'U':
                for a in range(0, int(f[1:])):
                    if grid[wire_pos_x][wire_pos_y] < 2:
                        grid[wire_pos_x][wire_pos_y] += 2
                    wire_pos_x -= 1
            elif f[0] == 'D':
                for a in range(0, int(f[1:])):
                    if grid[wire_pos_x][wire_pos_y] < 2:
                        grid[wire_pos_x][wire_pos_y] += 2
                    wire_pos_x += 1
    while not zip(*numpy.nonzero(grid == 3)):
        wire_pos_x = grid_center_x
        wire_pos_y = grid_center_y
        for f in wire_two:
            d += 1
            if f[0] == 'L':
                for a in range(0, int(f[1:])):
                    if grid[wire_pos_x][wire_pos_y] < 2:
                        grid[wire_pos_x][wire_pos_y] += 2
                    wire_pos_y -= 1
            elif f[0] == 'R':
                for a in range(0, int(f[1:])):
                    if grid[wire_pos_x][wire_pos_y] < 2:
                        grid[wire_pos_x][wire_pos_y] += 2
                    wire_pos_y += 1
            elif f[0] == 'U':
                for a in range(0, int(f[1:])):
                    if grid[wire_pos_x][wire_pos_y] < 2:
                        grid[wire_pos_x][wire_pos_y] += 2
                    wire_pos_x -= 1
            elif f[0] == 'D':
                for a in range(0, int(f[1:])):
                    if grid[wire_pos_x][wire_pos_y] < 2:
                        grid[wire_pos_x][wire_pos_y] += 2
                    wire_pos_x += 1


def part_one():
    wire_one = moves_into_moveset(moves[0])
    wire_two = moves_into_moveset(moves[1])
    moveset_into_instructions(0, wire_one)
    moveset_into_instructions(1, wire_two)
    find_distances()


def part_two():
    wire_one = moves_into_moveset(moves[0])
    wire_two = moves_into_moveset(moves[1])

    c = d = 0
    advance_wires(c, d, wire_one, wire_two)

    print(f'Part 2 answer: {c + d}')


if __name__ == '__main__':
    parser = ar.ArgumentParser(description='AoC 2019 - day 3')
    parser.add_argument('input', type=str, help='input file')
    args = parser.parse_args()

    moves = []

    try:
        moves = load_moves_list(args.input)
    except Exception as e:
        print(f'Could not process input file {e}')
        exit(1)

    square = 37000
    grid_width = square
    grid_height = square

    grid = numpy.zeros((grid_width, grid_height))
    grid_center_x = grid_width // 2
    grid_center_y = grid_height // 2
    part_one()
    print('Time spent: ', timeit.timeit(lambda: draw_grid()
                                        .save(f'day3_{args.input.split(".")[0]}.png',
                                              format='PNG'), number=1), 's')
    print('Time spent: ', timeit.timeit(lambda: part_two(), number=1), 's')
