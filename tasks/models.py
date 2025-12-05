from django.db import models

# Task model to store all to-do items
class Task(models.Model):
    # Status choices for the task
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    # Title of the task (required, max 200 characters)
    title = models.CharField(max_length=200)
    
    # Detailed description of the task (optional)
    description = models.TextField(blank=True)
    
    # Deadline for the task (optional)
    deadline = models.DateTimeField(null=True, blank=True)
    
    # Current status of the task (default is 'pending')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    
    # Automatically record when the task was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # String representation of the task (shows title)
    def __str__(self):
        return self.title
    
    # Order tasks by created date (newest first)
    class Meta:
        ordering = ['-created_at']
