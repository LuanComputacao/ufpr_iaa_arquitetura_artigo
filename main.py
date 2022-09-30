import pandas as pd
import pandas_profiling

from kdd import df_body_fat, heat_map_analysis, show_attibute_relations

SEPARATOR = '-' * 80

def main():
    df = df_body_fat
    print(df.dtypes)
    print(df.shape)
    print(df.describe())
    print(SEPARATOR )
    print(df.isnull().sum())
    print(SEPARATOR )
    density = df.Density
    print(density.head(3))
    print(SEPARATOR )
    df = pd.get_dummies(df)
    print(df.columns)
    # profile = pandas_profiling.ProfileReport(df_body_fat, title="Pandas Profiling Report")
    # profile.to_file("report.html")
    # show_attibute_relations(df_body_fat, 'BodyFat')
    # heat_map_analysis(df_body_fat)


if __name__ == '__main__':
    main()
