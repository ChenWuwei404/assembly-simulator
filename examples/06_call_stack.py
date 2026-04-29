from runner import run

run(
    """
        // USE M7 AS STACK TOP POINTER

        // INIT & BOOT
            ADD 255 0 M7
                // CALL `MAIN`
                WRITE M7 [0] -            // LOG RETURN POINT
                SUB M7 1 M7               // MOVE TOP
                JUMP [MAIN] - -           // JUMP TO `MAIN`
            STOP - - - <0>                // RETURN POINT


        // MAIN
            OUTPUT 0 - - <MAIN>
            ASCII 10 - -
            // CALL `FUNC`
                WRITE M7 [MAIN-R1] -
                SUB M7 1 M7
                JUMP [FUNC] - -
            // RETURN
                ADD M7 1 M7 <MAIN-R1>     // STACK POP
                READ M7 - M6
                JUMP M6 - -               // GOTO RETURN POINT


        // FUNC
            OUTPUT 128 - - <FUNC>
            // RETURN
                ADD M7 1 M7               // STACK POP
                READ M7 - M6
                JUMP M6 - -               // GOTO RETURN POINT
    """
)