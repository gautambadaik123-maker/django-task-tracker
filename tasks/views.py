from django.http import JsonResponse
from .models import Task

def task_list(request):
    """Fetches all tasks from the database and returns them as JSON data."""
    # Retrieve all tasks, grabbing only specific fields
    tasks = Task.objects.all().values('id', 'title', 'is_completed', 'created_at')
    
    # Return the data as a JSON response (standard for modern APIs)
    return JsonResponse({'tasks': list(tasks)}, safe=False)
