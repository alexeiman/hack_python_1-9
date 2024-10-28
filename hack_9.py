"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    x = 0
    while (x < len(result)):
        if (x%2==0):
            result.insert(x+1, "@")
        x += 1
    return result