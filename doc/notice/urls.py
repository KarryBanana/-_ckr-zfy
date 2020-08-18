from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('get_notice/',views.get_notice,name='get_notice'),
    path('read_notice/',views.read_notice,name="read_notice"),
    path('check_notice/',views.check_notice,name='check_notice'),
    path('delete_notice/',views.delete_notice,name='delete_notice'),
    path('clear_notice/',views.clear_notice,name="clear_notice"),
]