import pandas as pd
import re

df = pd.read_csv("data/processed/farmersmarkets_processed.csv", low_memory=False)

def return_valid_address(address):
    matched_address = re.findall("^(\d+) ?([A-Za-z](?= ))? (.*?) ([^ ]+?) ?((?<= )APT)? ?((?<= )\d*)?$", str(address))
    if len(matched_address) > 0:
        single_string = " ".join(matched_address[0]).strip()
        return ' '.join(single_string.split())

df['street_valid'] = df['street'].apply(return_valid_address)

df['full_address'] = df['street_valid'] + ", " + df['city_valid'] + ", " + df["State"] + " " + str(df["zip_valid"]).strip()

df.to_csv("data/processed/farmersmarkets_processed_with_address.csv")