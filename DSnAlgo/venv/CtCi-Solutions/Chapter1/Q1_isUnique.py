#O(N)
import unittest
def isUnique(str):
    if len(str)>128:
        return False
    char_set = [False for _ in range(128)]
    for char in str:
        val = ord(char)
        if(char_set[val]):
            #char already in string
            return False
        char_set[val]=True
    return True

print(isUnique("dipodaimary"))
print(isUnique("dipo"))

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        #true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)
        #false check
        for test_string in self.dataF:
            actual = isUnique(test_string)
            self.assertFalse(actual)
if __name__ == "__main__":
    unittest.main()
