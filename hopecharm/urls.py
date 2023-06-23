from django.urls import path
from . import views
app_name = 'hopecharm'

urlpatterns = [
    path('',views.index, name='index'), #config/urls -> matjipmrk/urls -> matjipmrk/views.py 실행!
    path('<int:board_id>/detail/', views.detail, name='detail'),
]