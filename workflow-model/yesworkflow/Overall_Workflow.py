# @BEGIN data_cleansing
# @IN raw_data @URI file:data/raw/farmersmarkets.csv
# @IN operation_history @URI file:open-refine/open_refine_extract_operation_history.json
# @IN transform_address_script @URI file:transform_address.py
# @OUT processed_data_with_address @URI file:data/processed/farmersmarkets_processed_with_address.csv

# @BEGIN open_refine_cleansing
# @IN raw_data @URI file:data/processed/farmersmarkets_processed.csv
# @IN operation_history @URI file:open-refine/open_refine_extract_operation_history.json
# @OUT processed_data @URI file:data/processed/farmersmarkets_processed.csv
# @END open_refine_cleansing

# @BEGIN process_addresses
# @IN processed_data @URI file:data/processed/farmersmarkets_processed.csv
# @IN transform_address_script @URI file:transform_address.py
# @OUT processed_data_with_address @URI file:data/processed/farmersmarkets_processed_with_address.csv
# @END process_addresses

# @END data_cleansing