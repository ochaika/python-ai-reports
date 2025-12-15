import pandas as pd

def analyze(df: pd.DataFrame) -> dict:
    summary = {
        'total_rows': len(df),
        'avg_sales': float(df['sales'].mean()),
        'max_sales': float(df['sales'].max()),
        'min_sales': float(df['sales'].min())
    }
    return summary


if __name__ == "__main__":
    from load_data import load_data

    df = load_data("data/sample.csv")   # ← df створюється ТУТ
    print(df.columns)                   # ← і тільки ПІСЛЯ цього його можна друкувати
    print(analyze(df))
