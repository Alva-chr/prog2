# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        Lst = [3,4,5,[2,3],3]
        self.assertEqual(count(1,[]), 0)
        self.assertEqual(count(3,Lst), 3)
        self.assertEqual(count([2,3],[3,[2,3],5,[2,3],3]), 2)
        self.assertEqual(count(4,[4,5,6,[4,5,[4,5],[4,5]],[4,5]]),5)
        self.assertEqual(count(1,[2,3,4,[5,6]]), 0)
        self.assertEqual(Lst, [3,4,5,[2,3],3])
        
        ''' Reasonable tests
        1. search empty lists (fixed)
        2. count first, last and interior elements (fixed)
        3. search for a list (fixed)
        4. check that sublists on several levels are searched (fixed)
        5. search non existing elements (fixed)
        6. check that the list searched is not destroyed (fixed)
        '''
        print('\nTests count')



if __name__ == "__main__":
    unittest.main()
