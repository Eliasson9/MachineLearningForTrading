import os
import pandas as pd
import matplotlib.pyplot as plt

class Utility:
    @staticmethod
    def fill_missing_values(df_data):
        """Fill missing values in data frame, in place."""
        df_data.fillna(method='ffill', inplace='TRUE')
        df_data.fillna(method='backfill', inplace='TRUE')
        return df_data

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