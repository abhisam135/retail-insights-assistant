import pandas as pd


def compute_metrics(df):

    if df.empty:
        return {"error": "Dataset is empty."}

    metrics = {}

    metrics["num_rows"] = df.shape[0]
    metrics["num_columns"] = df.shape[1]

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include="object").columns.tolist()

    metrics["numeric_columns"] = numeric_cols
    metrics["categorical_columns"] = categorical_cols

    # Numeric summaries
    metrics["numeric_summary"] = {}

    for col in numeric_cols:
        metrics["numeric_summary"][col] = {
            "sum": float(df[col].sum()),
            "mean": float(df[col].mean()),
            "min": float(df[col].min()),
            "max": float(df[col].max())
        }

    # Top categories
    metrics["top_categories"] = {}

    for col in categorical_cols[:5]:  # limit to avoid huge output
        metrics["top_categories"][col] = (
            df[col]
            .value_counts()
            .head(5)
            .to_dict()
        )

    return metrics