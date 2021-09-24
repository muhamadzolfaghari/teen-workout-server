from django.urls import path, include
from .views import UserList, UserDetail, UserDetailUpdate, UserDetailDestroy, UserDetailCreate
from loginapp.views import GoogleLogin

app_name = 'api' 

urlpatterns = [
    path('users/', UserList.as_view(), name='list' ),
    path('users/<int:pk>', UserDetail.as_view(), name='post' ),
    path('users/update/<int:pk>', UserDetailUpdate.as_view(), name='postupdate' ),
    path('users/delete/<int:pk>', UserDetailDestroy.as_view(), name='postdelete' ),
    path('users/create/', UserDetailCreate.as_view(), name='postcreate' ),
    path('auth/', include('rest_auth.urls')),
    path('auth/google/', GoogleLogin.as_view(), name='google_login')
]
