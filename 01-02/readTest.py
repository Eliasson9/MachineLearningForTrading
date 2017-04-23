import pandas as pa

def test_run():
    df = pa.read_csv("../data/AAPL.csv")
    print df;


if __name__ == "__main__":
    test_run()
