from flask import Flask, render_template
import weatherdf
import pandas as pd

app = Flask(__name__)

weather_stations = pd.read_csv('data_small/stations.txt', skiprows=17)
weather_stations = weather_stations[['STAID','STANAME                                 ']]

@app.route('/')
def home():
    return render_template('home.html', data=weather_stations.to_html())

@app.route('/api/v1/<station>/<date>')
def about(station, date):
    if(len(date) == 8):
        temp = weatherdf.get_station_data(station, date)
        return {'station': station,
              'date': date,
              'temperature': temp}
    return weatherdf.get_year_data(station, date)

@app.route('/api/v1/<station>')
def all_data(station):
    return weatherdf.get_all_data(station)


#__name__ only equals __main__ when this .py is run directly.
# This prevents other .py files that import this app from running the website while allowing them to use functions
if __name__ == '__main__':
    app.run(debug=True)