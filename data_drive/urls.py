from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.folder_list, name='folder_list'),
    path('folder/<int:folder_id>/', views.folder_detail, name='folder_detail'),
    path('file/<int:file_id>/', views.file_detail, name='file_detail'),
    path('folder/create/', views.folder_create, name='folder_create'),
    path('folder/create/<int:parent_folder_id>/', views.folder_create, name='folder_create'),  # Added this line
    path('file/create/<int:folder_id>', views.file_create, name='file_create'),
    path('folder/<int:folder_id>/update/', views.folder_update, name='folder_update'),
    path('file/<int:file_id>/update/', views.file_update, name='file_update'),
    path('folder/<int:folder_id>/delete/', views.folder_delete, name='folder_delete'),
    path('file/<int:file_id>/delete/', views.file_delete, name='file_delete'),
    path('folder/<int:parent_folder_id>/', views.folder_list, name='folder_list'),  # Added this line

]