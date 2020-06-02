from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.main, name='main_page'),
    path(r'new/post', views.new_post, name='new-post'),
    path(r'(<str:pk>)/', views.update_post, name='updatepost'),
    path(r'delete_post/(<int:pk>)/', views.delete_post, name='deletepost'),
    path(r'single/(<int:pk>)/', views.single_post, name = 'single_image'),
    path(r'search/', views.search_results, name='search_results'),
    path(r'comment/(<int:pk>)/', views.comments, name='add_comment'),
    path(r'likes/(<int:pk>)/' , views.like_images, name='likes'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)