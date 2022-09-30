import logging
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

FIG_SIZE = (15, 15)


def build_attibute_relations_subplot(data_set: pd.DataFrame, classification_column: str):
    columns = [
        (col)
        for col in sorted(
            list(
                set(data_set.columns)
                - {
                    classification_column,
                }
            )
        )
    ]

    len_columns = len(columns)
    fig, ax = plt.subplots(
        len_columns, len_columns, figsize=(15, 15), constrained_layout=False
    )

    for col in range(len_columns):
        for row in range(len_columns):
            ax[row, col].scatter(
                x=data_set[columns[col]], y=data_set[columns[row]], s=4
            )

            ax[row, col].set(
                xticks=[],
                yticks=[],
                xlabel=columns[col],
                ylabel=columns[row] if col == 0 else "",
            )

    plt.savefig(f"{os.getenv('REPORT_FIGURES_PATH')}/attribute_relation.png")
    logging.info("Attribute relation graph generated")
