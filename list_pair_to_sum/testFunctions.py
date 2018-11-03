import unittest
from hasPairFunctions import pairExistsWithSum_SortedList
from hasPairFunctions import pairExistsWithSum_unsortedOrSortedList

class TestPairFunctions(unittest.TestCase):

    def setUp(self):
        #sorted lists
        self.L0 = [1, 5, 6, 2, 8] #true expectation
        self.L1 = [1, 2, 3, 9, 17] #false expectation
        self.L2 = [1, 2, 4, 4, 5] #true expectation
        self.sum = 8

        #unsorted lists
        self.L3 = [10, 4, 6, 9, 5] #true expectation
        self.L4 = [1, 12, 7, 11, 2] #false expectation
        self.L5 = [8, 2, 5, 2, 3, 0, 7, 4, 1] #true expectation
        self.sum2 = 15

    def testSortedFunction(self):
        print("Sorted list function test:")

        self.assertTrue(pairExistsWithSum_SortedList(self.L0, self.sum))
        self.assertFalse(pairExistsWithSum_SortedList(self.L1, self.sum))
        self.assertTrue(pairExistsWithSum_SortedList(self.L2, self.sum))

    def testUnsortedOrSortedFunction(self):
        print("Unsorted list function test:")

        self.assertTrue(pairExistsWithSum_unsortedOrSortedList(self.L3, self.sum2))
        self.assertFalse(pairExistsWithSum_unsortedOrSortedList(self.L4, self.sum2))
        self.assertTrue(pairExistsWithSum_unsortedOrSortedList(self.L5, self.sum2))

if __name__ == '__main__':
    unittest.main()