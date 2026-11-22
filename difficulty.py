
import math
import random


def distance_km(first, second):
    lat1 = math.radians(first["lat"])
    lon1 = math.radians(first["lon"])
    lat2 = math.radians(second["lat"])
    lon2 = math.radians(second["lon"])

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )

    return 6371 * 2 * math.asin(min(1, math.sqrt(a)))


def choose_wrong_countries(countries, correct_country, difficulty):
    if difficulty not in ["Easy", "Medium", "Hard"]:
        raise ValueError("Unknown difficulty")

    other_countries = [
        country for country in countries
        if country["capital"] != correct_country["capital"]
    ]

    if len(other_countries) < 9:
        raise ValueError("At least 10 countries are needed")

    ordered = sorted(
        other_countries,
        key=lambda country: distance_km(correct_country, country)
    )

    pool_size = min(10, len(ordered) // 3)

    if difficulty == "Hard":
        pool = ordered[:pool_size]

    elif difficulty == "Medium":
        middle = len(ordered) // 2
        start = middle - pool_size // 2
        pool = ordered[start:start + pool_size]

    else:
        pool = ordered[-pool_size:]

    return random.sample(pool, 3)
