from flask import Flask, render_template

app = Flask('website')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<station>/<date>')
def about(station, date):
        return {'station': station,
                'date': date,
                'temperature': 0}

app.run(debug=True)