import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def heat_map_analysis(data_set: pd.DataFrame):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.widt', None)
    pd.set_option('display.max_colwidth', -1)
    
    corr = data_set.corr()
    print(corr)
    
    plt.subplots(figsize=(12,12))
    splot = sns.heatmap(corr, annot=True)
    sfig = splot.get_figure()
    sfig.savefig('./output/heat_map_atttribute_analysis.png', dpi = 300)
