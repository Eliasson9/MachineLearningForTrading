import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Util import get_data, plot_data, compute_daily_returns

def test_run():
    dates = pd.date_range('2009-01-01', '2016-12-31')
    symbols = ['SPY', 'IBM']
    df = get_data(symbols, dates)
    #plot_data(df)

    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily Returns")

    #Histogram
    mean = daily_returns['SPY'].mean()
    std = daily_returns['SPY'].std()
    daily_returns['SPY'].hist(bins=200, label='SPY')
    daily_returns['IBM'].hist(bins=200, label='IBM')
    plt.legend(loc='upper right')

    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()

    #Scatterplot
    daily_returns.plot(kind='scatter', x='SPY', y='IBM')

    beta_IBM, alpha_IBM = np.polyfit(daily_returns['SPY'], daily_returns['IBM'], 1)
    # k*x + m
    plt.plot(daily_returns['SPY'], beta_IBM*daily_returns['SPY'] + alpha_IBM, '-', color='r')

    plt.show()

    #Correlation
    print daily_returns.corr(method='pearson')

    # Kurtosis
    print daily_returns.kurtosis()

if __name__ == "__main__":
    test_run()