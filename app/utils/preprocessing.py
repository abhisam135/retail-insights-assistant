import pandas as pd


def load_and_clean_data(file):
    df = pd.read_csv(file, low_memory=False)

    # 1️⃣ Clean column names (safe for SQL)
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # 2️⃣ Try numeric conversion (safe)
    for col in df.columns:
        # Attempt numeric conversion only if column looks numeric
        if df[col].dtype == "object":
            cleaned = (
                df[col]
                .astype(str)
                .str.replace(r"[^\d\.\-]", "", regex=True)
            )

            numeric_version = pd.to_numeric(cleaned, errors="coerce")

            # Only convert if at least 50% values are numeric
            if numeric_version.notna().mean() > 0.5:
                df[col] = numeric_version

    # 3️⃣ Try datetime conversion (safe)
    for col in df.columns:
        if df[col].dtype == "object":
            if any(keyword in col.lower() for keyword in ["date", "time"]):
                parsed = pd.to_datetime(
                df[col],
                errors="coerce"   # Let pandas auto-detect format
                )
                if parsed.notna().mean() > 0.5:
                    df[col] = parsed
                   

    

    return df