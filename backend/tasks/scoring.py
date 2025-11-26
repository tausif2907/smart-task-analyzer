from dateutil import parser
from datetime import datetime, date
import math
def parse_date(d):
    if d is None:
        return None
    if isinstance(d, date):
        return d
    try:
        return parser.parse(d).date()
    except Exception:
        return None

def detect_cycles(tasks):
    # tasks: dict id -> task dict (with dependencies list)
    visited = {}
    stack = set()
    cycles = []
    def dfs(node):
        if node in stack:
            return [node]
        if node in visited:
            return []
        visited[node] = True
        stack.add(node)
        for dep in tasks.get(node, {}).get('dependencies', []):
            if dep in tasks:
                res = dfs(dep)
                if res:
                    cycles.append(res + [node])
        stack.remove(node)
        return []
    for n in list(tasks.keys()):
        dfs(n)
    return cycles

def compute_dependency_scores(tasks):
    # count how many tasks depend on a given task (directly)
    dep_count = {tid:0 for tid in tasks}
    for tid, t in tasks.items():
        for dep in t.get('dependencies', []):
            if dep in dep_count:
                dep_count[dep] += 1
    return dep_count

def urgency_score(due_date):
    today = date.today()
    if due_date is None:
        return 0.0
    delta = (due_date - today).days
    if delta < 0:
        # Overdue: high urgency; scale with how overdue (capped)
        return min(2.0, 1.0 + abs(delta)/7.0)
    # due in future: closer -> higher
    return max(0.0, 1.0 - delta/30.0)  # 0..1 roughly

def effort_score(hours):
    # lower hours -> higher quick-win score
    if hours is None or hours <= 0:
        return 1.0
    return 1.0 / (1.0 + math.log1p(hours))  # decreases with hours

def importance_score(importance):
    if importance is None:
        return 0.5
    return max(0.0, min(1.0, importance / 10.0))

def score_task(task, tasks_map, strategy='smart'):
    # normalize sub-scores to 0..1 or >1 for overdue handling
    d = parse_date(task.get('due_date'))
    u = urgency_score(d)
    e = effort_score(task.get('estimated_hours', 1.0))
    imp = importance_score(task.get('importance', 5))
    dep_counts = compute_dependency_scores(tasks_map)
    dep = dep_counts.get(task.get('id'), 0) if task.get('id') in dep_counts else 0
    dep_weight = min(1.0, dep / 5.0)  # cap

    # Different strategies
    if strategy == 'fastest':
        score = 0.6*e + 0.2*imp + 0.2*u + 0.4*dep_weight
    elif strategy == 'impact':
        score = 0.6*imp + 0.2*u + 0.1*e + 0.4*dep_weight
    elif strategy == 'deadline':
        score = 0.7*u + 0.15*imp + 0.15*e + 0.4*dep_weight
    else:  # smart balance
        score = 0.4*imp + 0.3*u + 0.2*e + 0.4*dep_weight

    # If overdue, boost score more
    if d and (d - date.today()).days < 0:
        score *= 1.2

    # ensure finite, normalized-ish
    return float(score)

def analyze_tasks(task_list, strategy='smart'):
    # convert to map for dependency resolution
    tasks_map = { (t.get('id') or str(i)): dict(t, id=(t.get('id') or str(i))) for i,t in enumerate(task_list) }
    # detect cycles
    cycles = detect_cycles(tasks_map)
    dep_counts = compute_dependency_scores(tasks_map)
    results = []
    for tid, task in tasks_map.items():
        s = score_task(task, tasks_map, strategy=strategy)
        explanation = []
        d = parse_date(task.get('due_date'))
        if d:
            days = (d - date.today()).days
            explanation.append(f"Due in {days} days" if days>=0 else f"Overdue by {abs(days)} days")
        explanation.append(f"Importance: {task.get('importance',5)}") 
        explanation.append(f"Estimated hours: {task.get('estimated_hours',1.0)}") 
        if dep_counts.get(tid,0)>0:
            explanation.append(f"Blocks {dep_counts[tid]} task(s)")
        results.append({
            'id': tid,
            'title': task.get('title'),
            'score': round(s,4),
            'explanation': '; '.join(explanation),
            'raw': task,
        })
    # sort desc by score
    results.sort(key=lambda x: x['score'], reverse=True)
    return {'results': results, 'cycles': cycles}
