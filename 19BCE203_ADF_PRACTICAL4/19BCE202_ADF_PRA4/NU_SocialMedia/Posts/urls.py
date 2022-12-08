from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('',postList.as_view(),name='postlist'),
    path('create/',postCreate.as_view(),name="postcreate"),
    path('<int:pk>',views.postlikeupdate,name="postupdatelike"),
    path('<int:pk>/update', views.postcomment,name='postcomment'),
     path('<int:pk>/comment',views.showcomment,name="showcomment"),
    # create one new url to call function for like increament
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
