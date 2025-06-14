# Weather Station API

## Description
A Flask-based REST API that retrieves historical weather data from different stations. Users can request temperature data for a specific station and date or an entire year's data.

## Features
- Fetch temperature data by station and date
- Retrieve full-year temperature records from a given station
- Display a list of available weather stations
- Converts temperature from deci-centigrade to Fahrenheit

## File Structure
- main.py: Defines Flask routes and handles API requests
- weatherdf.py: Processes station data, cleans inputs, and formats results
- data_small/: Contains station and temperature data file

## Practical Usages
- Climate Analysis: Analyzing historical temperature trends
- Weather Forecasting: Comparing past weather data for predictive models
- Research & Education: Providing easy access to weather records for studies

## Other Usages
This same framework could be used with other API data.  Examples include:
- Forcast/Supply Plan Trends
- Marketing/Sales Trends
- Operational Trends such as machine uptime and supplier performance