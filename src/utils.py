from typing import Sequence

from numpy import uint8

def int_to_hex(number: uint8) -> str:
    """Convert a `uint8` into hex

    e.g. `255` -> `00FF`

    Args:
        number (uint8): 

    Returns:
        str: 
    """
    return f"{int(number):04X}"

def uint8_sequence(sequence: Sequence[int]) -> Sequence[uint8]:
    return [uint8(item) for item in sequence]

if __name__ == "__main__":
    print(int_to_hex(uint8(0xFFFF)))
    