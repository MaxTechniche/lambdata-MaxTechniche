"""Basic unit test for DFunc BetterDF"""

import numpy as np
import pandas as pd
import unittest
from wrangle import BetterDF

DF1 = BetterDF({'A': range(20)})
DF2 = BetterDF({'B': (np.NaN for _ in range(20))})


class TestBetterDFMethods(unittest.TestCase):
    """Test BetterDF methods."""

    def test_numna(self):
        """Test BetterDF.numna method."""
        self.assertEqual(DF1.numna().values[0], 0)
        self.assertEqual(DF2.numna().values[0], 20)

    def test_train_test_split(self):
        """Test BetterDF.train_test_split method."""
        train, test = DF1.train_test_split(test_size=.2)
        self.assertEqual(len(test), 4)
        self.assertEqual(len(train), 16)
        train, test = DF1.train_test_split(test_size=.5)
        self.assertEqual(len(test), 10)
        self.assertEqual(len(train), 10)
        train, test = DF1.train_test_split(test_size=.75)
        self.assertEqual(len(test), 15)
        self.assertEqual(len(train), 5)

    def test_shuffle(self):
        """Test BetterDF.shuffle method."""
        shuffled = DF1.shuffle()
        self.assertTrue(list(shuffled.index) != list(DF1.index))
        df1 = list(DF1.index)
        df1_shuffled = list(DF1.shuffle(inplace=True).index)
        self.assertFalse(df1 == df1_shuffled)

if __name__ == "__main__":
    unittest.main()
