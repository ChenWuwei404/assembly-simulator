from runner import run

run(
    """
        INPUT - - M1 <2>
        EQ M1 0 [1]
        ADD M2 M1 M2
        JUMP [2] - -
        OUTPUT M2 - - <1>
        STOP - - - 
    """
)