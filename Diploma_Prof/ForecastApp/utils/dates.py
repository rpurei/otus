from config import DEBUG
from app_logger import logger_output
import pandas as pd
# from datetime import datetime, timedelta
import calendar


def create_df(start_date, end_date):
    try:
        df = pd.DataFrame(pd.date_range(start_date, end_date))
        df.columns = ['Date']
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df.drop(columns=['Date'], axis=1, inplace=True)
        df = df.groupby([(df.Year), (df.Month)]).sum()
        df = df.reset_index()
        df['Date'] = ''
        for index, row in df.iterrows():
            df.loc[index, (
                'Date')] = f'{df.loc[index, "Year"]}-{df.loc[index, "Month"] if df.loc[index, "Month"] > 9 else "0" + str(df.loc[index, "Month"])}-{calendar.monthrange(df.loc[index, "Year"], df.loc[index, "Month"])[1]}'
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        df.index = pd.DatetimeIndex(df.Date.values)
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Dayofweek'] = df['Date'].dt.dayofweek
        df.drop(columns=['Date'], axis=1, inplace=True)
        return df
    except Exception as err:
        logger_output(str(err), DEBUG, 'error')
