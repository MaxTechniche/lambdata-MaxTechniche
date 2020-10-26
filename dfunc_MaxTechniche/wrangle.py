"""Wrangle functions for pandas DataFrames"""

import pandas as pd
import numpy as np
import random

def numna(df):
    """Return number of null values in dataframe"""
    return df.isna().sum()

def train_test_split(df, test_size=.2, random_state=None):
    """Return a train/test split of a dataframe"""
    df_size = len(df)
    testing_size = max(1, int(df_size*test_size))
    test = df.sample(testing_size, random_state=random_state)
    train = df.drop(test.index)
    return train, test

def shuffle(df, random_state=None):
    """Return a shuffled version of the dataframe"""
    return df.sample(frac=1, random_state=random_state)
