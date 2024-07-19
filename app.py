from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    error = None
    if request.method == 'POST':
        city = request.form['cityName']
        try:
            data = get_weather(city)
        except Exception as e:
            error = str(e)
    return render_template('index.html', data=data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
