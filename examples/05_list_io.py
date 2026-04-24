from runner import run

run(
    """
        // INPUT AND WRITE TO RAM
        INPUT - - M1 <1>
        EQ M1 0 [2]
        WRITE M7 M1 -
        ADD M7 1 M7
        JUMP [1] - -

        // READ FROM RAM AND OUTPUT
        READ M6 - M1 <2>
        EQ M1 0 [3]
        OUTPUT M1 - -
        ASCII 10 - -
        ADD M6 1 M6
        JUMP [2] - -
        STOP - - - <3>
    """
)