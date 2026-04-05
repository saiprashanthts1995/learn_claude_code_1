import pandas as pd


def fn_createSampleDataframe() -> pd.DataFrame:
    """Create a pandas DataFrame with 3 columns and 5 rows."""
    data = {
        'column1': [1, 2, 3, 4, 5],
        'column2': ['a', 'b', 'c', 'd', 'e'],
        'column3': [10.5, 20.3, 30.1, 40.8, 50.2]
    }
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = fn_createSampleDataframe()
    print(df)
