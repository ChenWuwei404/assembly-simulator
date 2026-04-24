from judger import judge

# Task 05
#
#   Input a sequence of number until 0, and then output them in the reverse order.

code = """
    // Code here
    
    STOP - - -
"""


judge(code, l:=[10, 255, 114, 514, 191, 98, 10, 0], l[-2::-1])
judge(code, l:=[156, 41, 46, 45, 1, 7, 84, 156, 123, 22, 0], l[-2::-1])


print("All Tests Passed Successfully!")

# A possible answer encode in base64
# 