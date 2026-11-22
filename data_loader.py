
import json
import pandas as pd


def load_countries(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    df = pd.json_normalize(raw_data)

    df = df[
        ["name.common", "cca3", "capital", "flag",
         "region", "independent", "latlng"]
    ].copy()

    df.columns = [
        "country", "code", "capital", "flag",
        "region", "independent", "coordinates"
    ]

    df = df[df["independent"] == True].copy()

    df["capital"] = df["capital"].apply(
        lambda x: x[0] if isinstance(x, list) and len(x) == 1 else None
    )

    df["lat"] = df["coordinates"].apply(
        lambda x: x[0] if isinstance(x, list) and len(x) == 2 else None
    )

    df["lon"] = df["coordinates"].apply(
        lambda x: x[1] if isinstance(x, list) and len(x) == 2 else None
    )

    columns = ["country", "code", "capital", "flag", "region"]

    for column in columns:
        df[column] = df[column].astype("string").str.strip().replace("", pd.NA)

    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")

    df = df.dropna(subset=columns + ["lat", "lon"])

    df = df[
        df["lat"].between(-90, 90) &
        df["lon"].between(-180, 180)
    ]

    df = df.drop_duplicates(subset="code")
    df = df.drop_duplicates(subset="capital")

    df = df.drop(columns=["independent", "coordinates"])

    return df.reset_index(drop=True)
