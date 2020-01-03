import argparse as ar
import numpy


def load_moves_list(input_file) -> list:
    with open(input_file) as f:
        return f.readlines()


def moves_into_moveset(input_str) -> list:
    return input_str.split(',')


def move_wire(wire: int, direction: int, distance: int, posx, posy):
    for x in range (0, distance):
        if direction == 0:
            grid[posx - 1][posy] = 1 + wire
        elif direction == 1:
            grid[posx + 1][posy] = 1 + wire
        elif direction == 2:
            grid[posx][posy + 1] = 1 + wire
        elif direction == 3:
            grid[posx][posy - 1] = 1 + wire


def moveset_into_instructions(wire: int, moveset):
    wire_pos_x = 0
    wire_pos_y = 0
    for x in moveset:
        if x[0] == 'L':
            move_wire(wire, 3, x[1:], wire_pos_x, wire_pos_y)
        elif x[0] == 'R':
            move_wire(wire, 2, x[1:], wire_pos_x, wire_pos_y)
        elif x[0] == 'U':
            move_wire(wire, 0, x[1:], wire_pos_x, wire_pos_y)
        elif x[0] == 'D':
            move_wire(wire, 1, x[1:], wire_pos_x, wire_pos_y)


if __name__ == '__main__':
    parser = ar.ArgumentParser(description='AoC 2019 - day 3')
    parser.add_argument('input', type=str, help='input file')
    args = parser.parse_args()

    moves = []

    try:
        moves = load_moves_list(args.input)
    except Exception as e:
        print(f'Could not process input file')
        exit(1)

    grid_width = 8000
    grid_height = 8000
    grid = numpy.zeros((grid_width, grid_height))
    grid_center_x = grid_width // 2
    grid_center_y = grid_height // 2
    wire_one = moves_into_moveset(moves[0])
    wire_two = moves_into_moveset(moves[1])
    moveset_into_instructions(0, wire_one)
    moveset_into_instructions(1, wire_two)

