from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.loginUser, name='login'),
    path("register", views.registerUser, name='register'),
    path("logout", views.logoutUser, name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)