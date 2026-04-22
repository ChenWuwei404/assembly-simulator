from cpu import CPU
from ram import RAM

from compiler import compile

def run(code: str):
    cmd = RAM(256)

    cmd.update_commands(compile(code))

    ram = RAM(256)

    cpu = CPU(ram, cmd)

    cpu.run()
    while cpu.running:
        cpu.update()