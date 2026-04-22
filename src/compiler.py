from typing import Sequence

from numpy import uint8

from utils import uint8_sequence

command = {
    "STOP": 0b111111,
    "INPUT": 0b000000,
    "OUTPUT": 0b000001,
    "JUMP": 0b000010,

    "ADD": 0b010000,
    "SUB": 0b010001,
    "MUL": 0b010010,
    "DIV": 0b010011,

    "LS": 0b010100,
    "RS": 0b010101,
    "MOD": 0b010110,
    "NOT": 0b010111,

    "AND": 0b011000,
    "OR": 0b011001,
    "NAND": 0b011010,
    "NOR": 0b011011,

    "XOR": 0b011100,
    "XNOR": 0b011101,

    "NE": 0b001000,
    "EQ": 0b001001,
    "GT": 0b001010,
    "LT": 0b001100,
    "GE": 0b001011,
    "LE": 0b001101,
}

memories = {
    "P": 0b000,
    "M1": 0b001,
    "M2": 0b010,
    "M3": 0b011,
    "M4": 0b100,
    "M5": 0b101,
    "M6": 0b110,
    "M7": 0b111,
}

def compile_line(line: str) -> Sequence[uint8]:
    tokens = line.split('//')[0].strip().split()
    cmd_str = tokens[0]
    para1_str = tokens[1]
    para2_str = tokens[2]
    para3_str = tokens[3]

    cmd = command.get(cmd_str)
    if cmd is None:
        raise ValueError("Invalid Command")
    para1 = para2 = para3 = 0

    if para1_str in memories:
        cmd |= 0b10000000
        para1 = memories.get(para1_str)
        if para1 is None:
            raise ValueError("Invalid Memory ID")
    else:
        para1 = int(para1_str) if para1_str.isdigit() else 0

    if para2_str in memories:
        cmd |= 0b01000000
        para2 = memories.get(para2_str)
        if para2 is None:
            raise ValueError("Invalid Memory ID")
    else:
        para2 = int(para2_str) if para2_str.isdigit() else 0

    if para3_str in memories:
        para3 = memories.get(para3_str)
        if para3 is None:
            raise ValueError("Invalid Memory ID")
    else:
        para3 = int(para3_str) if para3_str.isdigit() else 0

    return uint8_sequence([cmd, para1, para2, para3])

def compile(code: str) -> list[Sequence[uint8]]:
    lines = code.splitlines()
    return [compile_line(line) for line in lines if line.strip()]

def print_bin(*numbers: uint8):
    print([bin(number) for number in numbers])

def print_bin_lines(*lines: Sequence[uint8]):
    for line in lines:
        print_bin(*line)

if __name__ == "__main__":
    print_bin_lines(*compile(
        """
        ADD 128 - M3

        SHOW M3 - -
        """
        ))