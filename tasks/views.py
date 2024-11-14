# tasks/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task, Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .serializers import TaskSerializer, CommentSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the user to the current logged-in user
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get', 'post'], url_path='tasks/(?P<task_id>[^/.]+)/comments')
    def task_comments(self, request, task_id=None):
        """Handles listing and creating comments for a specific task."""

        # Verify if the task exists
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise NotFound("Task not found.")

        if request.method == 'GET':
            comments = Comment.objects.filter(task=task)
            serializer = self.get_serializer(comments, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, task=task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
