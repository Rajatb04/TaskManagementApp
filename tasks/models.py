from django.db import models
from django.utils import timezone

class TaskType(models.TextChoices):
    DEVELOPMENT = 'DEV', 'Development'
    DESIGN = 'DSN', 'Design'
    TESTING = 'TST', 'Testing'
    MEETING = 'MTG', 'Meeting'
    OTHER = 'OTH', 'Other'

class TaskStatus(models.TextChoices):
    NOT_STARTED = 'NS', 'Not Started'
    IN_PROGRESS = 'IP', 'In Progress'
    COMPLETED = 'CP', 'Completed'
    ON_HOLD = 'OH', 'On Hold'

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    task_type = models.CharField(
        max_length=3, 
        choices=TaskType.choices, 
        default=TaskType.OTHER
    )
    
    status = models.CharField(
        max_length=2, 
        choices=TaskStatus.choices, 
        default=TaskStatus.NOT_STARTED
    )
    
    assigned_users = models.ManyToManyField(
        'users.User', 
        related_name='tasks', 
        blank=True
    )

    def __str__(self):
        return self.name

    def mark_completed(self):
        self.status = TaskStatus.COMPLETED
        self.completed_at = timezone.now()
        self.save()