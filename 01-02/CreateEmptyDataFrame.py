import pandas as pd

def test_run():
    #Define date range
    start_date = "2016-04-22"
    end_date = "2016-04-29"
    dates = pd.date_range(start_date, end_date)

    #Create an empty dataframe
    df1 = pd.DataFrame(index=dates)

    #Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("../data/SPY.csv",
                        index_col="Date",
                        parse_dates=True,
                        usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    dfSPY.rename(columns={'Adj Close', symbol})
    #Join two dataframes using Dataframe.join()
    #Does a left join by default
    df1 = df1.join(dfSPY, how="inner")

    #Drop nan values
    df1 = df1.dropna()

    print df1

if __name__ == "__main__":
    test_run()