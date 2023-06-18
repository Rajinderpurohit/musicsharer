from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.sign_page, name='sign'),
    path('t/', views.testing, name='testing'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home, name='home'),
    path('audio/', views.Audio_up_store, name='audio'),   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
