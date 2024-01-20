import mimetypes
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
load_dotenv()
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

TMDB_BASE_URI = "https://api.themoviedb.org/3"

def get_api_content(url):
    print(url)
    response = requests.request("GET", url)
    if response.status_code == 200:  # Check if the request was successful
        json_data = response.json()
        return json_data
    else:
        return str(response.content)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route("/main")
def mn():
    return render_template("index.html")

@app.route('/api/toprated-tv')
def get_toprated_tv(): return get_api_content(TMDB_BASE_URI + "/tv/top_rated?api_key=" + os.getenv("TMDB_API_KEY"))

@app.route('/api/popular-tv')
def get_latest_tv(): return get_api_content(TMDB_BASE_URI + "/tv/popular?api_key=" + os.getenv("TMDB_API_KEY"))

@app.route('/api/toprated-movies')
def get_toprated_movies(): return get_api_content(TMDB_BASE_URI + "/movie/top_rated?api_key=" + os.getenv("TMDB_API_KEY"))

@app.route('/api/popular-movies')
def get_latest_movies(): return get_api_content(TMDB_BASE_URI + "/movie/popular?api_key=" + os.getenv("TMDB_API_KEY"))

if __name__ == '__main__':
    app.run()