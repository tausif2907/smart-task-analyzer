from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .scoring import analyze_tasks
from rest_framework import status

@api_view(['POST'])
def analyze(request):
    data = request.data
    tasks = data.get('tasks') if isinstance(data, dict) else data
    strategy = (data.get('strategy') if isinstance(data, dict) else None) or request.query_params.get('strategy','smart')
    if not isinstance(tasks, list):
        return Response({'error':'expected list of tasks under key "tasks" or as JSON array'}, status=status.HTTP_400_BAD_REQUEST)
    # validate using serializer per-task
    serial = TaskSerializer(data=tasks, many=True)
    if not serial.is_valid():
        return Response({'error':'invalid tasks', 'details':serial.errors}, status=status.HTTP_400_BAD_REQUEST)
    analyzed = analyze_tasks(serial.validated_data, strategy=strategy)
    return Response(analyzed)

@api_view(['GET'])
def suggest(request):
    # for demo allow tasks via query param 'sample' or accept POST-like JSON via GET body (not typical)
    tasks = request.query_params.get('tasks_json')
    import json
    if tasks:
        try:
            tasks = json.loads(tasks)
        except:
            return Response({'error':'invalid tasks_json param'}, status=400)
    else:
        # fallback sample
        tasks = [
            { 'id':'1','title':'Sample A','due_date':None,'estimated_hours':1,'importance':6,'dependencies':[] },
            { 'id':'2','title':'Sample B','due_date':None,'estimated_hours':5,'importance':9,'dependencies':['1'] },
        ]
    analyzed = analyze_tasks(tasks, strategy='smart')
    top3 = analyzed['results'][:3]
    # add short explanations
    for t in top3:
        t['why'] = t['explanation']
    return Response({'suggestions': top3})
