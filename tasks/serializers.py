from rest_framework import serializers
from .models import Task, TaskType, TaskStatus
from users.models import User

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=User.objects.all(),
        required=False
    )
    
    assigned_user_details = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id', 
            'name', 
            'description', 
            'created_at', 
            'completed_at', 
            'task_type', 
            'status', 
            'assigned_users',
            'assigned_user_details'
        ]
        read_only_fields = ['created_at']

    def get_assigned_user_details(self, obj):
        return [
            {
                'id': user.id, 
                'name': user.name, 
                'email': user.email
            } 
            for user in obj.assigned_users.all()
        ]

    def create(self, validated_data):

        assigned_users = validated_data.pop('assigned_users', [])
        
        task = Task.objects.create(**validated_data)
        
        if assigned_users:
            task.assigned_users.set(assigned_users)
        
        return task