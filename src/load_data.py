import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, sep=",", engine="python")
    df.columns = df.columns.str.strip().str.lower()
    return df

if __name__ == "__main__":
    df = load_data("data/sample.csv")
    print(df.head())
