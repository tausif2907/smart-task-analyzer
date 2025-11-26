const API_BASE = "http://127.0.0.1:8000";

const tasks = [];
const resultsDiv = document.getElementById("results");
const jsonInput = document.getElementById("jsonInput");

document.getElementById("taskForm").addEventListener("submit", e => {
  e.preventDefault();
  const f = e.target;
  const t = {
    id: String(tasks.length + 1),
    title: f.title.value,
    due_date: f.due_date.value || null,
    estimated_hours: parseFloat(f.estimated_hours.value) || 1,
    importance: parseInt(f.importance.value) || 5,
    dependencies: f.dependencies.value ? f.dependencies.value.split(",").map(s=>s.trim()) : []
  };
  tasks.push(t);
  f.reset();
  renderTasks();
});

function renderTasks(){
  jsonInput.value = JSON.stringify(tasks, null, 2);
}

document.getElementById("analyzeBtn").addEventListener("click", async () => {
  let payload;
  const raw = jsonInput.value && jsonInput.value.trim();
  try {
    payload = raw ? JSON.parse(raw) : tasks;
    if (!Array.isArray(payload)) {
      // if user pasted an object {tasks:[...]}
      if (payload.tasks && Array.isArray(payload.tasks)) payload = payload.tasks;
      else throw new Error("JSON is not an array of tasks.");
    }
  } catch (err) {
    resultsDiv.innerHTML = "<div style='color:red'>Invalid JSON: " + err.message + "</div>";
    return;
  }

  const strategy = document.getElementById("strategy").value;
  resultsDiv.innerHTML = "Loading...";
  try {
    const API_BASE = "http://127.0.0.1:8000"; // backend URL
const res = await fetch(API_BASE + '/api/tasks/analyze/?strategy=' + encodeURIComponent(strategy), {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ tasks: payload, strategy })
});

    const data = await res.json();
    if (!res.ok) {
      resultsDiv.innerHTML = "<pre style='color:red'>" + JSON.stringify(data, null, 2) + "</pre>";
      return;
    }
    showResults(data.results);
  } catch (e) {
    resultsDiv.innerHTML = "<div style='color:red'>Error: " + e.message + "</div>";
    console.error(e);
  }
});

function showResults(list) {
  if (!list || list.length === 0) {
    resultsDiv.innerHTML = "<div>No tasks returned.</div>";
    return;
  }
  resultsDiv.innerHTML = "";
  for (const t of list) {
    const d = document.createElement("div");
    d.className = "task";
    const score = t.score;
    let cls = "low";
    if (score > 1.0) cls = "high";
    else if (score > 0.6) cls = "medium";
    d.classList.add(cls);
    d.innerHTML = `<strong>${t.title || "(no title)"}</strong> <em>(score: ${t.score})</em>
                   <div>${t.explanation || ""}</div>
                   <pre style="font-size:11px">${JSON.stringify(t.raw || t, null, 2)}</pre>`;
    resultsDiv.appendChild(d);
  }
}
