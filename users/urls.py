from django.urls import path

from users.apps import UsersConfig
from users.views import UserDetailAPIView, LoginUserView, ValidatePasscodeView, UserUpdateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('login_phone/', LoginUserView.as_view(), name='login_phone'),
    path('validate_code/', ValidatePasscodeView.as_view(), name='validate_passcode'),

    path('detail/<int:pk>/', UserDetailAPIView.as_view(), name='User_details'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='User_update'),
]
