from os import getenv

import pandas as pd


def get_df():
    return pd.read_csv(f"data/raw/{getenv('RAW_FILE_NAME')}.{getenv('RAW_FILE_EXTENSION')}")
