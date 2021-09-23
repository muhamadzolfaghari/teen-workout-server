from django.urls import path, include
from .views import UserList, UserDetail, UserDetailUpdate, UserDetailDestroy, UserDetailCreate, Logincud

app_name = 'api' 

urlpatterns = [
    path('users/', UserList.as_view(), name='list' ),
    path('users/<int:pk>', UserDetail.as_view(), name='post' ),
    path('users/update/<int:pk>', UserDetailUpdate.as_view(), name='postupdate' ),
    path('users/delete/<int:pk>', UserDetailDestroy.as_view(), name='postdelete' ),
    path('users/create/', UserDetailCreate.as_view(), name='postcreate' ),
    path('contacts/<int:pk>', Logincud.as_view(), name='login'),
]
