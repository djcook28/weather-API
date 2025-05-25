import pandas as pd
import numpy as np
import datetime

def clean_station(station_number):
    # zfill adds extra 0's to the string to make it the appropriate number of digits)
    return str(station_number).zfill(6)

def clean_date(date):
    return date[:4] + '-' + date[4:6] + '-' + date[6:]

def get_station_data(station_number, date):

    station_number = clean_station(station_number)
    date = clean_date(date)
    df = pd.read_csv(f'data_small/TG_STAID{station_number}.txt', parse_dates=['    DATE'], skiprows=20)
    #when data is unavailable temperature is defaulted to -9999, additionally temperatures are in deci centigrade so
    # masking all place holder values and dividing all values by 10
    df['TG'] = (df['   TG'].mask(df[' Q_TG']==9, np.nan)/10)
    df['Fahrenheit'] = (df['TG'] * (9/5)) + 32
    return df.loc[df['    DATE'] == date]['Fahrenheit'].squeeze()

def get_year_data(station_number, year):
    station_number = clean_station(station_number)
    df = pd.read_csv(f'data_small/TG_STAID{station_number}.txt', parse_dates=['    DATE'], skiprows=20)
    #when data is unavailable temperature is defaulted to -9999, additionally temperatures are in deci centigrade so
    # masking all place holder values and dividing all values by 10
    df['TG'] = (df['   TG'].mask(df[' Q_TG']==9, np.nan)/10)
    df['Fahrenheit'] = (df['TG'] * (9/5)) + 32
    df['Year'] = pd.to_datetime(df['    DATE']).dt.year
    df = df[df['Year'] == int(year)]
    return df[['STAID','    DATE','Fahrenheit']].to_dict(orient='records')

def get_all_data(station_number):

    station_number = clean_station(station_number)
    df = pd.read_csv(f'data_small/TG_STAID{station_number}.txt', parse_dates=['    DATE'], skiprows=20)
    #when data is unavailable temperature is defaulted to -9999, additionally temperatures are in deci centigrade so
    # masking all place holder values and dividing all values by 10
    df['TG'] = (df['   TG'].mask(df[' Q_TG']==9, np.nan)/10)
    df['Fahrenheit'] = (df['TG'] * (9/5)) + 32
    return df[['STAID','    DATE','Fahrenheit']].to_dict(orient='records')