import logging

import pandas as pd
import pandas_profiling
from dotenv import find_dotenv, load_dotenv

from kdd.data import get_df
from kdd.visualization import general_info

load_dotenv(find_dotenv())
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)

def main():
    df = get_df()
    general_info(df)
    # profile = pandas_profiling.ProfileReport(df_body_fat, title="Pandas Profiling Report")
    # profile.to_file("report.html")
    # show_attibute_relations(df_body_fat, 'BodyFat')
    # heat_map_analysis(df_body_fat)


if __name__ == '__main__':
    main()
