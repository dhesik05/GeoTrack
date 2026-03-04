from flask import Flask, render_template
from location_tracker import get_location

app = Flask(__name__)

@app.route("/")
def home():
    location = get_location()

    if location:
        lat, lon = location
    else:
        lat, lon = 0, 0

    return render_template("index.html", latitude=lat, longitude=lon)

if __name__ == "__main__":
    app.run(debug=True)