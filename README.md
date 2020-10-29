# Lambdata package by MaxTechniche

## (AKA) dfunc

dfunc holds a class called BetterDF that has additional functions for more efficient code writing.

## Main Features

* `.numna()`: returns the number of na values within the DataFrame
* `.train_test_split()`: Sets and returns a train test split on the DataFrame. Can accept `test_size`.
* `.shuffle()`: returns a shuffled version of the DataFrame. Can accept `inplace`.

`.train_test_split()` and `.shuffle()` accept `random_state`.

## How to to get it

```python
# TestPyPI
pip install -i https://test.pypi.org/simple/ dfunc

from dfunc.wrangle import BetterDF
```

pandas is the only dependency
