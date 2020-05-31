from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.main, name='main_page'),
    path('new/post', views.new_post, name='new-post'),
    path('profile/', views.profile, name = 'profile'),
    path(r'(<int:image_id>)/', views.single_post, name = 'single_image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)