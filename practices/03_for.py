from judger import judge

# Task 03
#
#   Input a number, then output from 1 to that number.

code = """
    // Code here

    STOP - - -
"""

judge(code, [10], [i for i in range(1, 10 + 1)])
judge(code, [1], [1])
judge(code, [128], [i for i in range(1, 128 + 1)])
judge(code, [0], [])

print("All Tests Passed Successfully!")

# A possible answer encode in base64
# SU5QVVQgLSAtIE0yCkVRIE0xIE0yIFsxXSA8Mj4KQUREIE0xIDEgTTEKT1VUUFVUIE0xIC0gLSAKSlVNUCBbMl0gLSAtIApTVE9QIC0gLSAtIDwxPg==