import pandas as pd

def get_df(filename):
    df = pd.read_excel(filename)
    print(df.Quantity.sum())
    df = df.dropna(subset=['ItemNo', 'ColorName'])
    return df

def get_sum(df):
    print("Hello")
    return df.Quantity.sum()