
import json
from urllib.request import urlopen

import pandas as pd


def load_population(year=2024):
    url = (
        "https://api.worldbank.org/v2/country/all/"
        f"indicator/SP.POP.TOTL?format=json&date={year}&per_page=1000"
    )

    with urlopen(url, timeout=30) as response:
        data = json.load(response)

    if not isinstance(data, list) or len(data) < 2 or not data[1]:
        raise ValueError("Population data is unavailable")

    rows = []

    for item in data[1]:
        if item["value"] is not None and item["countryiso3code"]:
            rows.append({
                "code": item["countryiso3code"],
                "population": item["value"],
                "year": int(item["date"])
            })

    df = pd.DataFrame(rows)

    if df.empty:
        raise ValueError("No population data found")

    df["population"] = pd.to_numeric(
        df["population"], errors="coerce"
    )

    df = df.dropna(subset=["population"])
    df = df[df["population"] > 0]
    df = df.drop_duplicates(subset="code")

    df["population"] = df["population"].astype("int64")

    return df.reset_index(drop=True)


def merge_population(countries, population):
    return countries.merge(
        population,
        on="code",
        how="inner",
        validate="one_to_one"
    )
