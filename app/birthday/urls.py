from django.urls import path
from . import views
from .views import Dashboard, IndexPage, CreateBirthday, DetailBirthday, UpdateBirthday, DeleteBirthday

urlpatterns = [
    path('', IndexPage.as_view(), name='index_url'),
    path('user-redirect', views.redirect_to_user_page, name='redirect_to_user_page'),
    path('dashboard/<int:pk>/', Dashboard.as_view(), name='dashboard_url'),
    path('create/<int:pk>/', CreateBirthday.as_view(), name='create_url'),
    path('detail/<int:pk>/', DetailBirthday.as_view(), name='detail_url'),
    path('update/<int:pk>/', UpdateBirthday.as_view(), name='update_url'),
    path('delete/<int:pk>/', DeleteBirthday.as_view(), name='delete_url'),
]
