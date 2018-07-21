"""
Implement an algorithm to determine whether string has all unique characters ?
--------------------------------------------------------------------------------
Solution1-->
import numpy as np
x = [1, 1, 1, 2, 3, 4, 5, 6, 2]
np.unique(x).size == len(x)
--------------------------------------------------------------------------------
Solution2-->
if len(x) > len(set(x)):
  print(False)
else
  print(True)
--------------------------------------------------------------------------------
Solution3-->Without using any external data structure.
"""
import unittest
def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
