from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addtodo, name='addtodo'),
    path('deletetodo/<int:todo_id>', views.deletetodo, name='deletetodo'),
    path('edittodo/<int:todo_id>', views.edittodo, name='edittodo'),
]