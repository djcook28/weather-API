from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def about(station, date):
        return {'station': station,
                'date': date,
                'temperature': 0}


#__name__ only equals itself when this .py is run directly.
# This prevents other .py files that import this app from running the website while allowing them to use functions
if __name__ == '__name__':
    app.run(debug=True)