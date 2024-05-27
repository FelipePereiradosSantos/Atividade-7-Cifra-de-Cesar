#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    
    res=""
    
    for i in range(len(s)):
    
        if s[i].isalpha():
    
            if s[i].isupper():
              res += chr(ord('A')+(ord(s[i])-ord('A')+k)%26)
    
            else:
              res += chr(ord('a')+(ord(s[i])-ord('a')+k)%26)
    
        else:
            res += s[i]
            
    return res
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
