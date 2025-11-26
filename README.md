# Task Analyzer - Complete Project (Generated)
This repository contains a complete implementation of the Smart Task Analyzer assignment.
It includes a Django backend (DRF) and a simple frontend (HTML/CSS/JS).

## Structure
- backend/: Django project and 'tasks' app
- frontend/: index.html, styles.css, script.js
- README.md (this file)

## Quick start (Linux / macOS)
1. Create virtualenv and install:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run migrations and start server:
   ```bash
   python manage.py migrate
   python manage.py runserver 8000
   ```
3. Serve the frontend (for development simply open `frontend/index.html` in browser).
   For proper API routing during development, run Django and open `http://127.0.0.1:8000/frontend/index.html`
   or serve static files via Django (not configured here) or use a lightweight server:
   ```bash
   cd frontend
   python -m http.server 8080
   ```
   Then open http://127.0.0.1:8080 in your browser.
4. Use the frontend to add tasks or paste JSON and click "Analyze Tasks".

## Algorithm (short)
The scoring algorithm combines:
- Urgency (due date proximity; overdue tasks boosted)
- Importance (1-10)
- Effort (lower estimated hours -> higher quick-win score)
- Dependencies (tasks that block others get a score bump)
There are 4 strategies: fastest, impact, deadline, smart (default).

## Tests
From `backend/` with the virtualenv activated:
```bash
python manage.py test tasks
```

## Files of interest
- backend/tasks/scoring.py -> scoring logic and analyze_tasks()
- backend/tasks/views.py -> API endpoints
- frontend/* -> simple UI that calls the API

## Notes & Next steps
- This is a compact implementation focused on the assignment requirements.
- You can extend the frontend to proxy API calls or integrate with Django templates.
- See backend/README_BACKEND.md for backend instructions.
