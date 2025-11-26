# Task Analyzer
A mini full-stack application that intelligently scores and prioritizes tasks based on urgency, importance, estimated effort, and dependency relationships.
This project includes a Django REST API backend and a vanilla HTML/CSS/JS frontend for task entry, analysis, and visualization.

📁 Project Structure
task-analyzer/
│
├── backend/
│   ├── manage.py
│   ├── task_analyzer/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── tasks/
│   │   ├── scoring.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── tests.py
│   └── requirements.txt
│
└── frontend/
    ├── index.html
    ├── styles.css
    └── script.js

🚀 Features
Backend

✔ Custom scoring algorithm
✔ Handles urgency, importance, effort, dependencies
✔ Detects circular dependencies
✔ Supports multiple prioritization strategies
✔ API endpoints built with Django REST Framework
✔ Unit tests included

Frontend

✔ Task entry form
✔ JSON bulk input
✔ Strategy selection dropdown
✔ API integration with backend
✔ Results displayed with color-coded priority indicators

⚙️ Setup Instructions

Follow these steps to run the project locally.

1. Backend Setup (Django)
Step 1 — Navigate into the backend folder
cd backend

Step 2 — Create and activate a virtual environment

Windows (PowerShell):

python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1

Step 3 — Install dependencies
pip install -r requirements.txt

Step 4 — Apply migrations
python manage.py migrate

Step 5 — Start the server
python manage.py runserver 8000


Backend runs at:

http://127.0.0.1:8000

2. Frontend Setup

Open a new terminal and run:

cd frontend
python -m http.server 8080


Frontend runs at:

http://127.0.0.1:8080


Make sure backend (port 8000) is running before testing the frontend.

📡 API Endpoints
POST /api/tasks/analyze/

Analyzes and returns sorted tasks with scores and explanations.

Sample Request Body

{
  "strategy": "smart",
  "tasks": [
    {
      "id": "1",
      "title": "Fix login issue",
      "due_date": "2025-11-30",
      "estimated_hours": 2,
      "importance": 8,
      "dependencies": []
    }
  ]
}

GET /api/tasks/suggest/

Returns top 3 recommended tasks with reasoning.

🧠 Scoring Algorithm Overview

The algorithm considers four major dimensions:

1. Urgency

Tasks closer to the due date score higher

Overdue tasks receive an additional boost

2. Importance

User-assigned weight from 1–10

3. Effort

Lower effort → higher score (quick wins)

Uses a logarithmic reduction for long tasks

4. Dependencies

Tasks that block other tasks get priority

Circular dependencies are detected and reported

Strategies Supported
Strategy	Description
Smart Balance	Considers all factors (default)
Fastest Wins	Favors low-effort tasks
High Impact	Favors importance
Deadline Driven	Favors urgency
🎛️ Frontend Usage Guide
Option 1 — Enter tasks individually

Fill out:

Title

Due date

Estimated hours

Importance

Dependencies (comma-separated IDs)

Click Add → then Analyze Tasks.

Option 2 — Use bulk JSON input

Example:

[
  {
    "id": "1",
    "title": "Fix error logs",
    "due_date": "2025-12-05",
    "estimated_hours": 2,
    "importance": 9,
    "dependencies": []
  },
  {
    "id": "2",
    "title": "Write report",
    "due_date": "2025-12-02",
    "estimated_hours": 1,
    "importance": 6,
    "dependencies": ["1"]
  }
]


Choose a strategy → Click Analyze Tasks.

Results

Sorted by score (highest first)

Color-coded:

🔴 High priority

🟡 Medium priority

🟢 Low priority

Each task includes an explanation:

Due date impact

Importance

Estimated hours

Dependency influence

🧪 Running Unit Tests

In the backend folder with venv active:

python manage.py test tasks

📸 Output

(Add your screenshots here)

Example:

<img width="1912" height="981" alt="image" src="https://github.com/user-attachments/assets/f800d9cc-b789-4490-a8d2-18e5afb72166" />
<img width="1891" height="1003" alt="image" src="https://github.com/user-attachments/assets/6143f27e-85e6-4ded-ba3a-a0ac032e8613" />

