# vue3-flask-moviedb-ui
This repository is a space to experiment with Vue 3 and Flask in order to create a basic UI to communicate with  free TMDB (The Movie DB) API

## Prerequisites

You will need to have python and Node.js installed to run this project.

This application was tested with Python 3.10 and Node.js 20.11

## Project setup

After cloning the repository, you will need to create a virtual python environment and install required packages:
```
cd server
python -m venv env
pip install -r requirements.txt
```

You will then need to obtain an API key for The Movie Database (TMDB).
Create a ```.env``` with the following contents:
```
TMDB_API_KEY=<your-key>
```
Be sure to replace ```<your_key>``` with your own API key.

## Running the project

### Flask server
switch to the server directory and use the following command to start the server:
```
flask run --port=5001 --debug
```

### Vue.js

Switch to the client directory and run the following commands:
```
npm install
npm run dev
```

## References

https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/