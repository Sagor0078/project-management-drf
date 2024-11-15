# projects/urls.py
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectMemberViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'project_members', ProjectMemberViewSet)

urlpatterns = router.urls
