from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, login, CurrentLoggedInUser, CategoryViewSet, NewsViewSet
router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'news', NewsViewSet)
urlpatterns = [
    path('login', login),
    path('register', RegisterUserView.as_view(), name="register"),
    path('user', CurrentLoggedInUser.as_view({'get': 'retrieve'}), name="current_user"),
    # path('category', CategoryViewSet.as_view({'get'}), name="category"),
    # path('news', NewsViewSet.as_view({'get': 'retrieve'}), name="news"),
    path("", include(router.urls))
    
]
