# Project: COLM website

This repo runs a Flask-based static-site server for the conference website.

## Quick start (local dev server)
1. Create and activate a virtualenv (recommended).
2. Install Python dependencies:
   - `pip install -r requirements.txt`
3. Start the dev server:
   - `make run`

The server listens on `http://localhost:5100`.

## Notes for web view
- If the web view needs a specific port, use `5100`.
- The site entry point is `/index.html`.
