"""Better pandas DataFrame."""

import pandas as pd


class BetterDF(pd.DataFrame):
    """Pandas DataFrame with a couple more simple functions."""

    def numna(self):
        """Returns the number of null values in dataframe."""
        return self.isna().sum()

    def train_test_split(self, test_size=.2, random_state=None):
        """Returns a train/test split of a dataframe."""
        df_size = len(self)
        testing_size = max(1, int(df_size*test_size))
        samp = self.sample(testing_size, random_state=random_state)
        self.test = BetterDF(samp)
        self.train = BetterDF(self.drop(self.test.index))

        return self.train, self.test

    def shuffle(self, random_state=None, inplace=False):
        """Returns a shuffled version of the dataframe."""
        df = BetterDF(self.sample(frac=1, random_state=random_state))
        if inplace:
            self = df
        return df

if __name__ == "__main__":
    df = BetterDF({
        'A': range(20),
        'B': range(20, 40)
    })

    df.train_test_split()
    df.shuffle()
    print(df.numna())
