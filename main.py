from flask import Flask, render_template
from weatherdf import get_station_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def about(station, date):

    temp = get_station_data(station.zfill(3), date)
    return {'station': station,
          'date': date,
          'temperature': temp}


#__name__ only equals __main__ when this .py is run directly.
# This prevents other .py files that import this app from running the website while allowing them to use functions
if __name__ == '__main__':
    app.run(debug=True)