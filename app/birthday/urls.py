from django.urls import path
from .import views
from .views import Dashboard, IndexPage, CreateBirthday

urlpatterns = [
    path('', IndexPage.as_view(), name='index_url'),
    path('dashboard/<int:pk>/', Dashboard.as_view(), name='dashboard_url'),
    path('create/<int:pk>/', CreateBirthday.as_view(), name='create_bday_url'),
]
