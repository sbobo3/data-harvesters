# %%
import re
import pandas as pd

# %%
df = pd.read_csv("data/processed/farmersmarkets_processed.csv", dtype=str)
df['street'] = str(df['street'])
df.info()

# %%
df['street'].head()

# %%
def return_valid_address(address):
    return re.findall("\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Pike|Pk|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?", 
    str(address))[0]

df['street_valid'] = df['street'].apply(lambda x: return_valid_address(x))

# %%
df.head()