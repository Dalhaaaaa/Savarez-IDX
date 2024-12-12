# blog/urls.py
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='blog-homepage'),
    path('<int:pk>/', views.blog_detail, name='blog-details'),
    path('create/', views.blog_create, name='blog-create'),
    path('update/<int:pk>/', views.blog_update, name='blog-update'),
    path('delete/<int:pk>/', views.blog_delete, name='blog-delete'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    # API routes
    path('api/', include('blog.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
