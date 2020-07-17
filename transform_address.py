import pandas as pd
import re

df = pd.read_csv("data/processed/farmersmarkets_processed.csv", low_memory=False)

df_cols = [
    "FMID",
    "MarketName",
    "Website",
    "Facebook",
    "Facebook_Link",
    "Twitter",
    "Twitter_Link",
    "Youtube",
    "Youtube_Link",
    "OtherMedia",
    "OtherMedia_Link",
    "street",
    "street_valid",
    "city",
    "city_valid",
    "County",
    "County_valid",
    "State",
    "zip",
    "zip_valid",
    "full_address",
    "Season1Date",
    "Season1StartDate",
    "Season1EndDate",
    "Season1Time",
    "Season2Date",
    "Season2StartDate",
    "Season2EndDate",
    "Season2Time",
    "Season3Date",
    "Season3StartDate",
    "Season3EndDate",
    "Season3Time",
    "Season4Date",
    "Season4StartDate",
    "Season4EndDate",
    "Season4Time",
    "longitude",
    "latitude",
    "Location",
    "Credit",
    "WIC",
    "WICcash",
    "SFMNP",
    "SNAP",
    "Organic",
    "Organic_valid",
    "Bakedgoods",
    "Cheese",
    "Crafts",
    "Flowers",
    "Eggs",
    "Seafood",
    "Herbs",
    "Vegetables",
    "Honey",
    "Jams",
    "Maple",
    "Meat",
    "Nursery",
    "Nuts",
    "Plants",
    "Poultry",
    "Prepared",
    "Soap",
    "Trees",
    "Wine",
    "Coffee",
    "Beans",
    "Fruits",
    "Grains",
    "Juices",
    "Mushrooms",
    "PetFood",
    "Tofu",
    "WildHarvested",
    "updateTime",
]


def return_valid_address(address):
    if address != None:
        matched_address = re.findall("^\d+\s[A-z.]+\s[A-z]+", str(address))
        if len(matched_address) > 0:
            return matched_address[0]


df["street_valid"] = df["street"].apply(return_valid_address)

df["full_address"] = (
    df["street_valid"]
    + ", "
    + df["city_valid"]
    + ", "
    + df["State"]
    + " "
    + df["zip_valid"]
)

df = df[df_cols]
df.to_csv("data/processed/farmersmarkets_processed_with_address.csv")
