import pandas as pd
import numpy as np
import datetime

def clean_parameters(station_number, date):
    # zfill adds extra 0's to the string to make it the appropriate number of digits)
    station_number = str(station_number).zfill(6)
    date = date[:4] + '-' + date[4:6] + '-' + date[6:]
    return station_number, date

def get_station_data(station_number, date):

    station_number, date = clean_parameters(station_number, date)

    df = pd.read_csv(f'data_small/TG_STAID{station_number}.txt', parse_dates=['    DATE'], skiprows=20)

    #when data is unavailable temperature is defaulted to -9999, additionally temperatures are in deci centigrade so
    # masking all place holder values and dividing all values by 10
    df['TG'] = (df['   TG'].mask(df[' Q_TG']==9, np.nan)/10)

    df['Fahrenheit'] = (df['TG'] * (9/5)) + 32

    return df.loc[df['    DATE'] == date]['Fahrenheit'].squeeze()