from typing import Callable, Any

from enum import IntEnum

from numpy import uint8, zeros

from numpy.typing import NDArray

from ram import RAM

class Command(IntEnum):
    STOP = 0b111111
    INPUT = 0b000000
    OUTPUT = 0b000001
    JUMP = 0b000010

    READ = 0b000100
    WRITE = 0b000101

    ASCII = 0b100000

    ADD = 0b010000
    SUB = 0b010001
    MUL = 0b010010
    DIV = 0b010011

    LS = 0b010100
    RS = 0b010101
    MOD = 0b010110
    NOT = 0b010111

    AND = 0b011000
    OR = 0b011001
    NAND = 0b011010
    NOR = 0b011011

    XOR = 0b011100
    XNOR = 0b011101

    NE = 0b001000
    EQ = 0b001001
    GT = 0b001010
    LT = 0b001100
    GE = 0b001011
    LE = 0b001101

class CPU:
    def __init__(
            self,
            ram: RAM,
            cmd: RAM,
            input_slot: Callable[[], uint8] = lambda: uint8(input("> ")),
            output_slot: Callable[[Any], None] = lambda x: print(x, end=''),  # type: ignore
        ) -> None:
        self.ram = ram
        self.cmd = cmd
        self.input_slot = input_slot
        self.output_slot = output_slot
        self.init()

    def init(self):
        self.caches: NDArray[uint8] = zeros((8), dtype=uint8)
        self.running = False

    def run(self):
        self.running = True

    @property
    def pointer(self) -> uint8:
        return self.caches[0]
    
    @pointer.setter
    def pointer(self, value: uint8):
        self.caches[0] = value

    def execute(self, cmd: uint8, para1: uint8, para2: uint8, para3: uint8) -> int:
        value1 = para1
        value2 = para2
        if cmd & 0b10000000:
            value1: uint8 = self.caches[para1]
        if cmd & 0b01000000:
            value2: uint8 = self.caches[para2]

        try:
            command = Command(int(cmd) & 0b00111111)
        except ValueError:
            return 4

        match command:
            case Command.STOP:
                self.running = False
            case Command.INPUT:
                self.caches[para3] = self.input_slot()
            case Command.OUTPUT:
                self.output_slot(value1)
            case Command.JUMP:
                self.pointer = value1
                return 0
            
            case Command.READ:
                self.caches[para3] = self.ram[int(value1)]
            case Command.WRITE:
                self.ram[int(value1)] = uint8(value2)
            
            case Command.ASCII:
                self.output_slot(chr(value1))

            case Command.ADD:
                self.caches[para3] = value1 + value2
            case Command.SUB:
                self.caches[para3] = value1 - value2
            case Command.MUL:
                self.caches[para3] = value1 * value2
            case Command.DIV:
                self.caches[para3] = value1 // value2

            case Command.LS:
                self.caches[para3] = value1 << value2
            case Command.RS:
                self.caches[para3] = value1 >> value2
            case Command.MOD:
                self.caches[para3] = value1 % value2
            case Command.NOT:
                self.caches[para3] = ~value1

            case Command.AND:
                self.caches[para3] = value1 & value2
            case Command.OR:
                self.caches[para3] = value1 | value2
            case Command.NAND:
                self.caches[para3] = ~(value1 & value2)
            case Command.NOR:
                self.caches[para3] = ~(value1 | value2)

            case Command.XOR:
                self.caches[para3] = value1 ^ value2
            case Command.XNOR:
                self.caches[para3] = ~(value1 ^ value2)

            case Command.NE:
                if value1 != value2:
                    self.pointer = para3
                    return 0
            case Command.EQ:
                if value1 == value2:
                    self.pointer = para3
                    return 0
            case Command.GT:
                if value1 > value2:
                    self.pointer = para3
                    return 0
            case Command.LT:
                if value1 < value2:
                    self.pointer = para3
                    return 0
            case Command.GE:
                if value1 >= value2:
                    self.pointer = para3
                    return 0
            case Command.LE:
                if value1 <= value2:
                    self.pointer = para3
                    return 0

            case _:
                return 4
        return 4
            
    def update(self):
        if self.running:
            step = self.execute(*self.cmd[self.pointer:self.pointer + 4])
            self.pointer = self.pointer + step