import logging


def general_info(df):
    logging.info(df.dtypes)
    logging.info(df.shape)
    logging.info(df.describe())
    logging.info(df.isnull().sum())
    
    
