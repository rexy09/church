from django.urls import path
from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('register-user', views.register_user, name='register-user'),
    path('list-user', views.list_user, name='list-user'),
    path('view-user/<int:id>', views.view_user, name='view-user'),
    path('edit-user/<int:id>', views.edit_user, name='edit-user'),
    path('delete-user/<int:id>', views.delete_user, name='delete-user'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('change-password', views.change_password, name='change-password'),
    path('profile', views.profile_view, name='profile'),
]
