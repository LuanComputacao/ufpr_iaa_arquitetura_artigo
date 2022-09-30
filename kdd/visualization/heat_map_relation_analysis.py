import logging
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def heat_map_analysis(data_set: pd.DataFrame):
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.widt", None)
    pd.set_option("display.max_colwidth", None)

    corr = data_set.corr()

    plt.subplots(figsize=(12, 12))
    splot = sns.heatmap(corr, annot=True)
    sfig = splot.get_figure()
    sfig.savefig(
        f"{os.getenv('REPORT_FIGURES_PATH')}/heat_map_atttribute_analysis.png", dpi=300
    )
    logging.info("Attribute relation heatmap graph generated")
