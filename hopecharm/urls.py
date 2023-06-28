from django.urls import path
from . import views


app_name = 'hopecharm'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:board_id>/detail/', views.detail, name='detail'),
    # path('hopecharm/<int:pk>/detail', ),
]