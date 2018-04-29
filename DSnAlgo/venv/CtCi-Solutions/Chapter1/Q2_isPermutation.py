from collections import Counter
import unittest

def isPermutation(str1,str2):
    counter = Counter()
    for c in str1:
        counter[c]+=1
    for c in str2:
        if counter[c]==0:
            return False
        counter[c]-=1
    return True

dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
dataF = (
    ('abcd', 'd2cba'),
    ('2354', '1234'),
    ('dcw4f', 'dcw5f'),
)
print(isPermutation('abcd', 'bacd'))
print(isPermutation('abcd', 'bacde'))
