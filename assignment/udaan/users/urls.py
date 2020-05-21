from django.urls import path, URLPattern
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from users.views import UserViewSet, CustomUserListView

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls

urlpatterns += format_suffix_patterns([
    path('user-list/', CustomUserListView.as_view(), name='users-ljhist'),
])
