# All data parser functions

import pandas as pd

from helpers.constants import DATA_FILE


def get_data() -> pd.DataFrame:
    return pd.read_stata(DATA_FILE)


def run():
    data = get_data()
    print(data)
