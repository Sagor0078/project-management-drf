from django.test import TestCase

# Create your tests here.
# # """"""
# from django.test import TestCase
# from .models import Project, ProjectMember, CustomUser
# from .serializers import ProjectSerializer, ProjectMemberSerializer

# class ProjectSerializerTests(TestCase):

#     def setUp(self):
#         self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')
#         self.project_attributes = {
#             'name': 'Test Project',
#             'description': 'Test Description',
#             'owner': self.user,
#             'created_at': '2023-01-01T00:00:00Z'
#         }
#         self.project = Project.objects.create(**self.project_attributes)
#         self.serializer = ProjectSerializer(instance=self.project)

#     def test_contains_expected_fields(self):
#         data = self.serializer.data
#         self.assertEqual(set(data.keys()), set(['id', 'name', 'description', 'owner', 'created_at']))

#     def test_name_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['name'], self.project_attributes['name'])

#     def test_description_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['description'], self.project_attributes['description'])

#     def test_owner_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['owner'], self.user.id)

#     def test_created_at_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['created_at'], self.project_attributes['created_at'])

# class ProjectMemberSerializerTests(TestCase):

#     def setUp(self):
#         self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')
#         self.project = Project.objects.create(
#             name='Test Project',
#             description='Test Description',
#             owner=self.user,
#             created_at='2023-01-01T00:00:00Z'
#         )
#         self.project_member_attributes = {
#             'project': self.project,
#             'user': self.user,
#             'role': 'member'
#         }
#         self.project_member = ProjectMember.objects.create(**self.project_member_attributes)
#         self.serializer = ProjectMemberSerializer(instance=self.project_member)

#     def test_contains_expected_fields(self):
#         data = self.serializer.data
#         self.assertEqual(set(data.keys()), set(['id', 'project', 'user', 'role']))

#     def test_project_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['project'], self.project.id)

#     def test_user_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['user'], self.user.id)

#     def test_role_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['role'], self.project_member_attributes['role'])