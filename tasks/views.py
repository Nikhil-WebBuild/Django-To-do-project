from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task

# View to display all tasks
def task_list(request):
    """
    This view displays all tasks in the database.
    We get all tasks from the database and pass them to the template.
    """
    tasks = Task.objects.all()  # Get all tasks from database
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# View to add a new task
def add_task(request):
    """
    This view handles creating a new task.
    When the user submits the form (POST), we create the task.
    When the user first visits the page (GET), we show them an empty form.
    """
    if request.method == 'POST':
        # Get data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status', 'pending')
        
        # Create a new task object
        task = Task(
            title=title,
            description=description,
            status=status
        )
        
        # Only add deadline if user provided one
        if deadline:
            task.deadline = deadline
        
        # Save the task to database
        task.save()
        
        # Redirect back to the task list page
        return redirect('task_list')
    
    # If GET request, just show the form
    return render(request, 'tasks/task_form.html', {
        'action': 'Add',
        'status_choices': Task.STATUS_CHOICES
    })


# View to update an existing task
def update_task(request, task_id):
    """
    This view handles editing an existing task.
    We find the task by its ID, then update it with new data from the form.
    """
    # Get the task or show 404 error if it doesn't exist
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        # Update task with new data from form
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        
        deadline = request.POST.get('deadline')
        if deadline:
            task.deadline = deadline
        else:
            task.deadline = None
        
        # Save changes to database
        task.save()
        
        # Go back to task list
        return redirect('task_list')
    
    # If GET request, show the form with existing task data
    return render(request, 'tasks/task_form.html', {
        'action': 'Update',
        'task': task,
        'status_choices': Task.STATUS_CHOICES
    })


# View to delete a task
def delete_task(request, task_id):
    """
    This view deletes a task from the database.
    We find the task by ID and delete it.
    For security, this view only accepts POST requests.
    """
    # Get the task or show 404 error if it doesn't exist
    task = get_object_or_404(Task, id=task_id)
    
    # Only delete if this is a POST request (for security)
    if request.method == 'POST':
        # Delete the task from database
        task.delete()
    
    # Go back to task list
    return redirect('task_list')

