from flask import Flask, send_file, request, make_response, render_template
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anime-image')
def serve_image():
    response = make_response(send_file("destination/anime.webp", mimetype='image/jpeg'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


def update_images():
    print("Updating images... 🚀")
    try:
        # Run your existing image update script
        subprocess.run(["python", "script.py"], check=True)
        print("Images updated successfully! 🌟")
    except Exception as e:
        print(f"Error updating images: {e}")


# Set up a scheduler to run the update_images function every 5 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(update_images, "interval", minutes=2)
scheduler.start()


if __name__ == '__main__':
    print(sys.executable)
    app.run(debug=True, use_reloader=False)
