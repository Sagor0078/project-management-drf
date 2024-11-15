from django.test import TestCase

# Create your tests here.
# FILE: test_serializers.py
# from .models import Task, Comment, CustomUser
# from .serializers import TaskSerializer, CommentSerializer


# class TaskSerializerTests(TestCase):

#     def setUp(self):
#         self.user = CustomUser.objects.create_user(
#             username="testuser", email="testuser@example.com", password="testpass123"
#         )
#         self.task_attributes = {
#             "title": "Test Task",
#             "description": "Test Description",
#             "status": "open",
#             "priority": "high",
#             "assigned_to": self.user,
#             "project": "Test Project",
#             "created_at": "2023-01-01T00:00:00Z",
#             "due_date": "2023-01-10T00:00:00Z",
#         }
#         self.task = Task.objects.create(**self.task_attributes)
#         self.serializer = TaskSerializer(instance=self.task)

#     def test_contains_expected_fields(self):
#         data = self.serializer.data
#         self.assertEqual(
#             set(data.keys()),
#             set(
#                 [
#                     "id",
#                     "title",
#                     "description",
#                     "status",
#                     "priority",
#                     "assigned_to",
#                     "project",
#                     "created_at",
#                     "due_date",
#                 ]
#             ),
#         )

#     def test_title_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["title"], self.task_attributes["title"])

#     def test_description_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["description"], self.task_attributes["description"])

#     def test_status_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["status"], self.task_attributes["status"])

#     def test_priority_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["priority"], self.task_attributes["priority"])

#     def test_assigned_to_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["assigned_to"], self.user.id)

#     def test_project_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["project"], self.task_attributes["project"])

#     def test_created_at_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["created_at"], self.task_attributes["created_at"])

#     def test_due_date_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["due_date"], self.task_attributes["due_date"])


# class CommentSerializerTests(TestCase):

#     def setUp(self):
#         self.user = CustomUser.objects.create_user(
#             username="testuser", email="testuser@example.com", password="testpass123"
#         )
#         self.task = Task.objects.create(
#             title="Test Task",
#             description="Test Description",
#             status="open",
#             priority="high",
#             assigned_to=self.user,
#             project="Test Project",
#             created_at="2023-01-01T00:00:00Z",
#             due_date="2023-01-10T00:00:00Z",
#         )
#         self.comment_attributes = {
#             "content": "Test Comment",
#             "user": self.user,
#             "task": self.task,
#             "created_at": "2023-01-02T00:00:00Z",
#         }
#         self.comment = Comment.objects.create(**self.comment_attributes)
#         self.serializer = CommentSerializer(instance=self.comment)

#     def test_contains_expected_fields(self):
#         data = self.serializer.data
#         self.assertEqual(
#             set(data.keys()), set(["id", "content", "user", "task", "created_at"])
#         )

#     def test_content_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["content"], self.comment_attributes["content"])

#     def test_user_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["user"], self.user.id)

#     def test_task_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["task"], self.task.id)

#     def test_created_at_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data["created_at"], self.comment_attributes["created_at"])
