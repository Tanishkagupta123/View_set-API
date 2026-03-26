from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='students'),
router.register(r'employee', StudentViewSet, basename='employee'),

urlpatterns = router.urls
