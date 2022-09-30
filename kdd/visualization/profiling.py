import logging

from pandas import DataFrame


def general_info(df: DataFrame, data_type_sulfix: str) -> None:
    with open(f"reports/general_info_of_{data_type_sulfix}.txt", "w") as file:
        separator = f'\n{"-" * 80}\n'
        file.write(f"Number of rows: {df.shape[0]} {separator}")
        file.write(f"Number of columns: {df.shape[1]} {separator}")
        file.write(f"Column names: {df.columns} {separator}")
        file.write(f"Column types: {df.dtypes} {separator}")
        file.write(f"Number of null values: {df.isnull().sum().sum()} {separator}")
        file.write(f"Number of unique values: {df.nunique().sum()} {separator}")
        file.write(f"Number of duplicated rows: {df.duplicated().sum()} {separator}")
        file.write(f"Number of unique values per column: {df.nunique()} {separator}")
        file.write(f"Number of null values per column: {df.isnull().sum()} {separator}")
        file.write(
            f"Number of duplicated rows per column: {df.duplicated().sum()} {separator}"
        )
        file.write(f"DataFrame Description: {df.describe()} {separator}")
        logging.info("General info saved to file")


def generate_profiling_report(df):
    profile = df.profile_report(title="Pandas Profiling Report")
    profile.to_file(output_file="reports/profiling_report.html")
    logging.info("Profiling report generated")
