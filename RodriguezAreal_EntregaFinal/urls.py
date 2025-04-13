"""
URL configuration for RodriguezAreal_EntregaFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog import views  # Importa views desde el archivo actual
from blog.views import BlogListView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from blog.views import blog_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # Vista 'Acerca de mí'
    path('profile/', views.profile, name='profile'),  # Vista de perfil
    path('blog/blog_lst', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-post/', views.add_post, name='add_post'),
    path('buscar-post/', views.search_post, name='search_post'),
    path('blogs/<int:pk>/eliminar/', blog_delete, name='blog_delete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)