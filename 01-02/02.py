import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    df = df.ix[start_index : end_index]
    plot_data(df[columns])

def normalize_data(df):
    return df /df.ix[0 , :]

def get_data(symbols, dates):
    #Create an empty dataframe
    df=pd.DataFrame(index=dates)

    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    #Read all data into temporary dataframe
    for symbol in symbols:
        df_temp = pd.read_csv('../data/{}.csv'.format(symbol), index_col='Date',
                                parse_dates=True, usecols=['Date', 'Adj Close'],
                                na_values=['nan'])

        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])

    return df

def plot_data(df, title='Stock Prices'):
    ax = df.plot(title = title, fontsize = 2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()


def test_run():
    #Define date range
    start_date = '2010-01-01'
    end_date = '2010-12-31'
    dates=pd.date_range(start_date, end_date)
    print dates
    print dates[0]

    #Create an empty dataframe
    df1=pd.DataFrame(index=dates)
    print df1

    #Read SPY data into temporary dataframe
    dfSPY = pd.read_csv('../data/SPY.csv', index_col='Date',
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    dfSPY = dfSPY.rename(columns={'Adj Close' : 'SPY'})

    #Join the two dataframes using DataFrame.join()
    #inner join removes all NaN in this case
    df1 = df1.join(dfSPY, how='inner')
    print df1

    #Remove all NaN
    df1 = df1.dropna()
    print df1

    symbols = ['GOOG', 'IBM', 'GLD']

    for symbol in symbols:
        df_temp = pd.read_csv('../data/{}.csv'.format(symbol), index_col='Date',
                                parse_dates=True, usecols=['Date', 'Adj Close'],
                                na_values=['nan'])

        df_temp = df_temp.rename(columns={'Adj Close' : symbol})

        df1 = df1.join(df_temp)
        print df1

    df = get_data(symbols, dates)
    print df
    print df.mean()
    print df.median()
    print df.std()
    df = normalize_data(df)
    plot_data(df)
    #plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')

if __name__ == '__main__':
    test_run()
