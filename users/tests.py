from django.test import TestCase

# # FILE: test_serializers.py
# from django.test import TestCase
# from .models import CustomUser
# from .serializers import UserSerializer, CustomDjoserUserSerializer

# class UserSerializerTests(TestCase):

#     def setUp(self):
#         self.user_attributes = {
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'first_name': 'Test',
#             'last_name': 'User'
#         }
#         self.user = CustomUser.objects.create(**self.user_attributes)
#         self.serializer = UserSerializer(instance=self.user)

#     def test_contains_expected_fields(self):
#         data = self.serializer.data
#         self.assertEqual(set(data.keys()), set(['id', 'username', 'email', 'first_name', 'last_name']))

#     def test_username_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['username'], self.user_attributes['username'])

#     def test_email_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['email'], self.user_attributes['email'])

#     def test_first_name_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['first_name'], self.user_attributes['first_name'])

#     def test_last_name_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['last_name'], self.user_attributes['last_name'])

# class CustomDjoserUserSerializerTests(TestCase):

#     def setUp(self):
#         self.user_attributes = {
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'first_name': 'Test',
#             'last_name': 'User'
#         }
#         self.user = CustomUser.objects.create(**self.user_attributes)
#         self.serializer = CustomDjoserUserSerializer(instance=self.user)

#     def test_contains_expected_fields(self):
#         data = self.serializer.data
#         self.assertIn('id', data)
#         self.assertIn('username', data)
#         self.assertIn('email', data)
#         self.assertIn('first_name', data)
#         self.assertIn('last_name', data)

#     def test_username_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['username'], self.user_attributes['username'])

#     def test_email_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['email'], self.user_attributes['email'])

#     def test_first_name_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['first_name'], self.user_attributes['first_name'])

#     def test_last_name_field_content(self):
#         data = self.serializer.data
#         self.assertEqual(data['last_name'], self.user_attributes['last_name'])