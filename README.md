# Task Analyzer

A mini full-stack application that intelligently scores and prioritizes tasks based on urgency, importance, estimated effort, and dependency relationships.  
This project includes:

- A **Django REST API backend**
- A **vanilla HTML/CSS/JS frontend** for task entry, analysis, and visualization

---

## Project Structure
```
task-analyzer/
│
├── backend/
│ ├── manage.py
│ ├── requirements.txt
│ ├── task_analyzer/
│ │ ├── settings.py
│ │ ├── urls.py
│ │ ├── wsgi.py
│ ├── tasks/
│ │ ├── models.py
│ │ ├── scoring.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── tests.py
│
├── frontend/
│ ├── index.html
│ ├── styles.css
│ ├── script.js
```

---

## Backend Features

- Custom multi-factor task scoring algorithm
- Supports urgency, due dates, importance, effort, and dependencies
- Detects and reports circular dependencies
- Multiple prioritization strategies (Smart Balance, Urgency-First, Impact-First, etc.)
- Django REST Framework API endpoints
- Unit tests included

---

## Frontend Features

- Simple task entry form  
- JSON bulk task input  
- Strategy selection dropdown  
- API integration with backend  
- Color-coded result display  
- Clear score explanation per task  

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally.

---

### **1️⃣ Backend Setup (Django)**

#### Step 1 — Navigate into the backend folder
```
cd backend
```
Step 2 — Create and activate a virtual environment
Windows (PowerShell):

```bash

python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```
Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```
Step 4 — Apply migrations
```bash
python manage.py migrate
```
Step 5 — Start the backend server
```bash
python manage.py runserver 8000
```
Backend will now be running at:
```
http://127.0.0.1:8000
```

---

### **2️⃣ Frontend Setup**
Open a new terminal and navigate to the frontend folder:
```
cd frontend
```
Start a simple HTTP server:
```bash
python -m http.server 8080
```
Frontend will be available at:
```
http://127.0.0.1:8080
```

---

### **API Endpoints**
Analyze Tasks

POST /api/tasks/analyze/?strategy=smart
JSON Body Example:

```json
{
  "tasks": [
    {
      "id": "1",
      "title": "Fix login",
      "due_date": "2025-11-30",
      "estimated_hours": 2,
      "importance": 8,
      "dependencies": []
    }
  ]
}
```

---

### **Output**

Output Example 1:
<img width="1919" height="983" alt="image" src="https://github.com/user-attachments/assets/c0683a78-a35c-4ed9-b85a-baeaf72aeae9" />
<img width="1919" height="1008" alt="image" src="https://github.com/user-attachments/assets/70b8ee7d-19bd-401d-aad7-5d4af6fc5fae" />

Output Example 2:
<img width="1919" height="640" alt="image" src="https://github.com/user-attachments/assets/23e4e393-1db6-4386-9775-f354d0df7ae3" />
<img width="1919" height="508" alt="image" src="https://github.com/user-attachments/assets/54a1a238-7807-4625-97c8-11f66021c530" />
<img width="1919" height="993" alt="image" src="https://github.com/user-attachments/assets/9682927d-5f5c-46e1-99f5-65a398b2f144" />


---

### **Running Unit Tests**
```
python manage.py test tasks
```
---

### **Summary**
This project is a compact full-stack application demonstrating:

- Django REST API development
- Custom business logic (task scoring)
- Frontend-to-backend communication
- Clean separation between UI and backend logic
