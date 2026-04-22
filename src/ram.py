from typing import overload, Sequence

from numpy import uint8, zeros

class RAM:
    def __init__(self, size: int) -> None:
        self.data = zeros((size), dtype=uint8)

    def update_commands(self, commands: Sequence[Sequence[uint8]]) -> None:
        for i, command in enumerate(commands):
            self.data[i*4:(i+1)*4] = command

    @overload
    def __getitem__(self, key: int) -> uint8: ...
    @overload
    def __getitem__(self, key: slice) -> list[uint8]: ...
    def __getitem__(self, key: int | slice):
        if isinstance(key, int) and 0 <= key < self.data.shape[0]:
            return self.data[key]
        elif isinstance(key, slice) and 0 <= key.start < self.data.shape[0] and 0 <= key.stop <= self.data.shape[0]:
            return self.data[key]
        raise IndexError()
    
    @overload
    def __setitem__(self, key: int, value: uint8) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Sequence[uint8]) -> None: ...
    def __setitem__(self, key: int | slice, value: uint8 | Sequence[uint8]) -> None:
        if isinstance(key, int) and 0 <= key < self.data.shape[0]:
            self.data[key] = value
        elif isinstance(key, slice) and 0 <= key.start < self.data.shape[0] and 0 <= key.stop <= self.data.shape[0]:
            self.data[key] = value
        else:
            raise IndexError()