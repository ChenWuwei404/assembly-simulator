from judger import judge

# Task 05
#
#   Input a sequence of number until 0, and then output them in the reverse order.

code = """
    // Code here

    STOP - - -
"""


judge(code, l:=[10, 255, 114, 145, 191, 98, 10, 0], l[-2::-1])
judge(code, l:=[156, 41, 46, 45, 1, 7, 84, 156, 123, 22, 0], l[-2::-1])


print("All Tests Passed Successfully!")

# A possible answer encode in base64
# Ly8gSU5QVVQgQU5EIFdSSVRFCklOUFVUIC0gLSBNMSA8Mj4KRVEgTTEgMCBbMV0KV1JJVEUgTTcgTTEgLQpBREQgTTcgMSBNNwpKVU1QIFsyXSAtIC0KCi8vIFJFQUQgQU5EIE9VVFBVVApTVUIgTTcgMSBNNyA8MT4KRVEgTTcgMjU1IFszXQpSRUFEIE03IC0gTTEKT1VUUFVUIE0xIC0gLQpKVU1QIFsxXSAtIC0KU1RPUCAtIC0gLSA8Mz4=