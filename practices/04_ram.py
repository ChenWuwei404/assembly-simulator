

# Task 04
#
#   Write to each byte in RAM a value equal to its own address.

code = """
    // Code here
    ADD M7 1 M7 <1>
    WRITE M7 M7 -
    NEQ M7 255 [1]
    STOP - - -
"""


def test():
    from ram import RAM
    from cpu import CPU
    from compiler import compile

    cmd = RAM(256)

    cmd.update_commands(compile(code))

    ram = RAM(256)

    cpu = CPU(ram, cmd)

    cpu.run()
    while cpu.running:
        cpu.update()

    if ram.data != [i for i in range(256)]:
        raise 
test()
print("All Tests Passed Successfully!")

# A possible answer encode in base64
# QUREIE03IDEgTTcgPDE+CldSSVRFIE03IE03IC0KTkVRIE03IDI1NSBbMV0KU1RPUCAtIC0gLQ==