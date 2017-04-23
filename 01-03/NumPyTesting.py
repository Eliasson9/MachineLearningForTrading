import pandas as pd
import numpy as np
import time
from Utility.Utility import Utility

def fill_missing_values(df_data):
    """Fill missing values in data frame, in place."""
    ##########################################################
    df_data.fillna(method='ffill', inplace='TRUE')
    df_data.fillna(method='backfill', inplace='TRUE')
    return df_data
    ##########################################################

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['AAPL', 'IBM', 'GLD']
    # Get stock data
    df = Utility.get_data(symbols, dates)
    # print df
    #Utility.plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')
    Utility.plot_data(df)
    print df.mean()
    print df.median()
    print df.std()

def test_run2():
    #1D array
    print np.array([2, 3, 4])

    #2D array
    print np.array([(2, 3, 4), (5, 6, 7)])

    #Empty array
    print np.empty((5, 4))

    #Array with ones
    print np.ones((5, 4), dtype=np.int_) #float by default

    #Generare random numbers
    print np.random.rand(5, 4)

    #Sample numbers from a Gaussian (normal) distribution
    print np.random.normal(size=(2, 3))

    # Random Integers
    print np.random.randint(10) # a single integer in [0, 10]
    print np.random.randint(0, 10) # same as above but explicit definition
    print np.random.randint(0, 10, size=5) # 5 random integers as a 1D array
    print np.random.randint(0, 10, size=(2, 3)) # 2x3 array of random integer

    a = np.random.random((5, 4))
    print a.shape[0] # nr rows
    print a.shape[1] # nr cols

    print len(a.shape) #dimension

    print a.size # 4x5 = 20
    print a.dtype

def test_runOperations():
    np.random.seed(693) # seed the random generator
    a = np.random.randint(0, 10, size=(5, 4))
    print "Array:\n", a

    # print the sum of all elements
    print "Sum of all elements:", a.sum()
    print "Sum of all cols:", a.sum(axis=0)
    print "Sum of all rows:", a.sum(axis=1)

    # Statistics
    print "Minimum of each col:\n", a.min(axis=0)
    print "Maximum of each row:\n", a.max(axis=1)
    print "Mean of all elements:\n", a.mean()

    print np.unravel_index(np.argmax(a), a.shape)

if __name__ == "__main__":
    test_run()