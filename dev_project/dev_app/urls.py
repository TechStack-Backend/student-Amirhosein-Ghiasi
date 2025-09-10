from django.urls import path
from .views import developers_list, developer_cv

urlpatterns = [
    path('developers/', developers_list, name='developers_list'),
    path('developers/<str:username>/', developer_cv, name='developer_cv'),
]