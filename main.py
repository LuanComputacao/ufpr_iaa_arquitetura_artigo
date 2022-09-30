import logging

import pandas as pd
import pandas_profiling
from dotenv import find_dotenv, load_dotenv

from kdd.data import get_df
from kdd.visualization import (build_attibute_relations_subplot, general_info,
                               generate_profiling_report, heat_map_analysis)

load_dotenv(find_dotenv())
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)

def main():
    df_raw = get_df()
    general_info(df_raw, "raw")
    generate_profiling_report(df_raw)
    build_attibute_relations_subplot(df_raw, 'BodyFat')
    heat_map_analysis(df_raw)


if __name__ == '__main__':
    main()
