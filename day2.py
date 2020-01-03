import argparse as ar
import timeit


def load_instruction_list(input_file) -> str:
    with open(input_file) as f:
        return f.read()


def ins_into_list(input_string: str) -> list:
    return [int(x) for x in input_string.split(',')]


def process_instructions(ins: list) -> list:
    x = 0
    ins[1] = 12
    ins[2] = 2
    while x < len(ins):
        if ins[x] == 99:
            return ins
        elif ins[x] == 1:
            a_pos = ins[x+1]
            b_pos = ins[x+2]
            res_pos = ins[x+3]
            ins[res_pos] = ins[a_pos] + ins[b_pos]
        elif ins[x] == 2:
            a_pos = ins[x + 1]
            b_pos = ins[x + 2]
            res_pos = ins[x + 3]
            ins[res_pos] = ins[a_pos] * ins[b_pos]
        x += 4

    return ins


def part2_processing(ins: list) -> int:
    memory = ins.copy()
    for x in range(0, 99):
        for y in range(0, 99):
            ins = memory.copy()
            ins[1] = x
            ins[2] = y
            a = 0
            while a < (len(ins) - 4):
                if ins[a] == 99:
                    a = 999
                elif ins[a] == 1:
                    a_pos = ins[a + 1]
                    b_pos = ins[a + 2]
                    res_pos = ins[a + 3]
                    if a_pos < len(ins) and b_pos < len(ins) and res_pos < len(ins):
                        ins[res_pos] = ins[a_pos] + ins[b_pos]
                elif ins[a] == 2:
                    a_pos = ins[a + 1]
                    b_pos = ins[a + 2]
                    res_pos = ins[a + 3]
                    if a_pos < len(ins) and b_pos < len(ins) and res_pos < len(ins):
                        ins[res_pos] = ins[a_pos] * ins[b_pos]
                a += 4
                if ins[0] == 19690720:
                    return (100 * x) + y


if __name__ == '__main__':
    parser = ar.ArgumentParser(description='AoC 2019 - day 2')
    parser.add_argument('input', type=str, help='input file')

    args = parser.parse_args()
    ins_str = ''

    try:
        ins_str = load_instruction_list(args.input)
    except Exception as e:
        print(f'Could not process input file')
        exit(1)

    ins_list = ins_into_list(ins_str)
    ins_list_dva = ins_list.copy()

    print('Part one result: ', process_instructions(ins_list.copy())[0])
    print('Part two result: ', part2_processing(ins_list_dva))


