from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# from .views import UserRole

app_name = 'users'

urlpatterns = [
    # path('', login_required(UserRole.as_view()), name='users'),
]
