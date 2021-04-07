import sys

CUR_STATE = 0
CUR_SYMBOL = 1
NEW_SYMBOL = 2
DIRECTION = 3
NEW_STATE = 4

# codigo para marcar o inicio da fita (£)
mark_init = [
    ["0", "*", "*", "l", "1'"],
    ["1'", "*", "£", "r", "0'"],
]

# codigo para marcar o inicio (£) e fim da fita (¢) 
mark_init_and_end = [
    ["0", "0", "£", "r", "1'"],
    ["0", "1", "£", "r", "2'"],
    ["1'", "0", "0", "r", "1'"],
    ["1'", "1", "0", "r", "2'"],
    ["1'", "_", "0", "r", "3'"],
    ["2'", "0", "1", "r", "1'"],
    ["2'", "1", "1", "r", "2'"],
    ["2'", "_", "1", "r", "3'"],
    ["3'", "_", "¢", "l", "3'"],
    ["3'", "0", "0", "l", "3'"],
    ["3'", "1", "1", "l", "3'"],
    ["3'", "£", "£", "r", "0'"],
]

# 
def move_all_to_right(state):
    """
        codigo para movimentar toda a fita um espaço para direita
    """
    aux_state = f'{state}£'
    return [
        [state, "£", "£", "r", aux_state],
        [aux_state, "0", "_", "r", f"1'{state}£"],
        [aux_state, "1", "_", "r", f"2'{state}£"],
        [aux_state, "_", "_", "r", f"3'{state}£"],
        [f"1'{state}£", "0", "0", "r", f"1'{state}£"],
        [f"1'{state}£", "1", "0", "r", f"2'{state}£"],
        [f"1'{state}£", "_", "_", "r", f"3'{state}£"],
        [f"1'{state}£", "¢", "0", "r", f"4'{state}£"],
        [f"2'{state}£", "0", "1", "r", f"1'{state}£"],
        [f"2'{state}£", "1", "1", "r", f"2'{state}£"],
        [f"2'{state}£", "_", "_", "r", f"3'{state}£"],
        [f"2'{state}£", "¢", "1", "r", f"4'{state}£"],
        [f"3'{state}£", "0", "_", "r", f"1'{state}£"],
        [f"3'{state}£", "1", "_", "r", f"2'{state}£"],
        [f"3'{state}£", "_", "_", "r", f"3'{state}£"],
        [f"3'{state}£", "¢", "_", "r", f"4'{state}£"],
        [f"4'{state}£", "_", "¢", "l", f"5'{state}£"],
        [f"5'{state}£", "_", "_", "l", f"5'{state}£"],
        [f"5'{state}£", "1", "1", "l", f"5'{state}£"],
        [f"5'{state}£", "0", "0", "l", f"5'{state}£"],
        [f"5'{state}£", "£", "£", "r", state],
    ]


def split_command(command: str):
    return command.replace("\n", "").split(" ")


def join_command(splited_command: [str]):
    return " ".join(splited_command) + "\n"


def convert_infinite(code: [str]):
    """
    Converte infinito para semi infinito
    """
    output = [";S"] + mark_init_and_end
    states = {}
    for line in code:
        curr_command = split_command(line)

        if curr_command[CUR_STATE] == "0":
            curr_command[CUR_STATE] = "0'"
        if curr_command[NEW_STATE] == "0":
            curr_command[NEW_STATE] = "0'"

        if curr_command[CUR_STATE] not in states:
            states[curr_command[CUR_STATE]] = True

        output.append(curr_command)

    for state in states:
        open_end_state = f"{state}¢"
        output.append([state, "¢", "_", "r", open_end_state])
        output.append([open_end_state, "_", "¢", "l", state])
        output += move_all_to_right(state)

    return output


def convert_semi_infinite(code: [str]):
    """
    Converte semi infinito para infinito
    """
    output = [";I"] + mark_init
    for line in code:
        curr_command = split_command(line)

        if curr_command[CUR_STATE] == "0":
            curr_command[CUR_STATE] = "0'"
        if curr_command[NEW_STATE] == "0":
            curr_command[NEW_STATE] = "0'"

        output.append(curr_command)

    # se encontrar o simbolo inicial simula a barreira a esquerda
    output.append(["*", "£", "£", "r", "*"])

    return output


def parse_mt_file(path: str):
    try:
        input_file = open(path, "r")
        lines = input_file.readlines()
        input_file.close()
        output = None

        if ";" not in lines[0]:
            raise Exception("Missing first line comment")

        if "I" in lines[0]:
            output = convert_infinite(lines[1:])
        elif "S" in lines[0]:
            output = convert_semi_infinite(lines[1:])
        else:
            raise Exception(
                "First comment line need to contain [I] infinite or [S] semi-infinite"
            )

        output_file = open(path.split(".")[0] + ".out.txt", "w")
        for line in output:
            output_file.write(join_command(line))
        output_file.close()

    except FileNotFoundError:
        print(f'File "{path}" not found')
        exit(0)


if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        parse_mt_file(input_file)

    except IndexError:
        print("Missing input file path")
        exit(1)
