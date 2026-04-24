from runner import run

run(
    """
        INPUT - - M1
        WRITE 0 M1 -
        READ 0 - M2
        OUTPUT M2 - -
        STOP - - -
    """
)