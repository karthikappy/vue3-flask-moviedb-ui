# vue3‑flask‑moviedb‑ui – A lightweight Vue 3 + Flask SPA that proxies the TMDB API

This repository demonstrates a minimal **single‑page application** that connects a **Vue 3** frontend to a **Flask** backend.  The backendBell serves as a thin proxy layer for the free public `TMDB` (The Movie Database) API, while the frontend consumes those endpoints and shows popular movies, search results, and poster grids.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Backend Setup](#backend-setup)
4. [Frontend Setup](#frontend-setup)
5. [References](#references)

---

## Prerequisites

| Tool | Minimum version | Tested version |
|------|------------------|----------------|
| Python | 3.10+ | 3.10.x |
| Node.js | 20.11+ | 20.11.x |

Verify the installed versions:

```bash
python --version   # outputs something like Python 3.10.12
node --version      # outputs something like v20.11.0
```

---

## Project Structure

```text
├── backend/          # Flask API – see backend/app.py
├── frontend/         # Vue 3 SPA – see frontend/src
└── README.md
``` 

---

## Backend (Flask API)

1. **Create a virtual environment** (the project does not ship a Python environment, so you’ll need to set one up locally):
   ```bash
   cd backend
   python -m venv .venv
   # On Windows:
   # .venv\Scripts\activate
   # On macOS/Linux:
   # source .venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the TMDB API key**: Create a `.env` file in the `backend/` directory with:
   ```dotenv
   TMDB_API_KEY=<your‑TMDB‑api‑key>
   ```
   The `.env` file is included in `.gitignore` by default.

4. **Start the Flask server**: By default it listens on **port 5001**.
   ```bash
   flask run --port=5001 --debug
   ```
   *The `--debug` flag enables auto‑reload & detailed error logs.*

---

## Frontend (Vue 3 SPA)

1. **Install JavaScript dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Run the development server**:
   ```bash
   npm run dev
   ```
   Vite will serve the app on `http://localhost:5173`.  Hot‑module replacement is enabled.

3. **Build for production** (optional):
   ```bash
   npm run build
   ```
   The compiled assets are placed under `frontend/dist`.

---

## References

- [TMDB API Documentation](https://developers.themoviedb.org)
- [Vue 3 Documentation](https://vuejs.org)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Vuetify UI Library](https://vuetifyjs.com)

---

If you’d like to see the code in action, follow the above steps: start the Flask backend first, then run the Vue 3 dev server.  The app will automatically make requests to `http://localhost:5001/api/...` and present the results in the browser.
