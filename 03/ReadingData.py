"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt

class Utility:
    @staticmethod
    def symbol_to_path(symbol, base_dir="../data"):
        """Return CSV file path given ticker symbol."""
        return os.path.join(base_dir, "{}.csv".format(str(symbol)))

    @staticmethod
    def get_data(symbols, dates):
        """Read stock data (adjusted close) for given symbols from CSV files."""
        df = pd.DataFrame(index=dates)
        if 'SPY' not in symbols:  # add SPY for reference, if absent
            symbols.insert(0, 'SPY')

        for symbol in symbols:
            df = df.join(
                pd.read_csv(
                    Utility.symbol_to_path(symbol),
                    index_col="Date",
                    parse_dates=True,
                    usecols=["Date", "Adj Close"],
                    na_values=['NaN']
                ).rename(
                    columns={ 'Adj Close': symbol }
                )
            )
            if symbol == 'SPY':
                df = df.dropna(subset=['SPY'])

        return df

    @staticmethod
    def normalize_data(df):
        """Normalize stock prices using the first row of the dataframe"""
        return df / df.ix[0, :]

    @staticmethod
    def plot_data(df, title="Stock prices"):
        """Plot stock prices"""

        ax = df.plot(title=title)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        plt.show()

    @staticmethod
    def plot_selected(df, columns, start_index, end_index):
        """Plot the desired columns over index values in the given range."""

        Utility.plot_data(df.ix[start_index:end_index, columns])

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    # Get stock data
    df = Utility.get_data(symbols, dates)
    #print df
    Utility.plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')

    #Slicing by row
    #print df.ix['2010-01-01':'2010-01-31']

    #Slice by column
    #print df['GOOG']
    #print df[['IBM', 'SPY']]

    #Slice by row and col
    #print df.ix['2010-03-10':'2010-03-15', ['SPY', 'IBM']]

    #Normalize the data
    #df1 = df1/df1[0]




if __name__ == "__main__":
    test_run()