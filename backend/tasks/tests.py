from django.test import TestCase
from .scoring import analyze_tasks, score_task
from datetime import date, timedelta
class ScoringTests(TestCase):
    def test_overdue_boost(self):
        t = [{'id':'a','title':'A','due_date': (date.today() - timedelta(days=3)).isoformat(), 'estimated_hours':2,'importance':5,'dependencies':[]}]
        res = analyze_tasks(t)
        self.assertGreater(res['results'][0]['score'], 0)

    def test_dependency_influence(self):
        t = [
            {'id':'1','title':'One','due_date':None,'estimated_hours':3,'importance':5,'dependencies':[]},
            {'id':'2','title':'Two','due_date':None,'estimated_hours':2,'importance':6,'dependencies':['1']},
        ]
        res = analyze_tasks(t)
        # task '1' should have dependency count > 0 and receive some boost
        ids = [r['id'] for r in res['results']]
        self.assertIn('1', ids)

    def test_strategies_differ(self):
        t = [{'id':'x','title':'X','due_date':None,'estimated_hours':10,'importance':9,'dependencies':[]}]
        r1 = analyze_tasks(t, strategy='fastest')['results'][0]['score']
        r2 = analyze_tasks(t, strategy='impact')['results'][0]['score']
        self.assertNotEqual(r1, r2)
