from django.urls import path
from .views import *

urlpatterns = [

    # path('', ProfileList.as_view())
    path('',userList.as_view(),name='userlist'),
    path('create/',userCreate.as_view(),name="usercreate"),
    # path('<int:pk>/',userDetail.as_view(),name="userdetail"),
    # path('<int:pk>/update/',userUpdate.as_view(),name="userupdate"),
    # path('<int:pk>/delete/',userDelete.as_view(),name="userdelete"),
]