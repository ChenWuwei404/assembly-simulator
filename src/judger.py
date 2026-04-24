from typing import Any, Sequence

from numpy import uint8

from utils import uint8_sequence

from compiler import compile

from ram import RAM
from cpu import CPU

class InputStream:
    def __init__(self, *args: uint8) -> None:
        self.items = list(args)

    def __call__(self) -> uint8:
        if self.items:
            return self.items.pop(0)
        raise IndexError("Too much INPUT args required")
    
class OutputStream:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def __call__(self, arg: Any):
        self.items.append(arg)

def judge(code: str, inputs: Sequence[int], outputs: list[Any]) -> None:
    input_stream = InputStream(*uint8_sequence(inputs))
    output_stream = OutputStream()

    cmd = RAM(256)

    cmd.update_commands(compile(code))

    ram = RAM(256)

    cpu = CPU(ram, cmd, input_stream, output_stream)

    cpu.run()
    while cpu.running:
        cpu.update()

    if output_stream.items != outputs:
        raise AssertionError(f"Expected output {outputs}, but got {output_stream.items}")