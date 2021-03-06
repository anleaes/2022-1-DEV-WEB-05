from django.urls import path
from . import views

app_name = 'tipos'

urlpatterns = [
    path('', views.list_tipos, name='list_tipos'),
    path('adicionar/', views.add_tipo, name='add_tipo'),
    path('editar/<int:id_tipo>/', views.edit_tipo, name='edit_tipo'),
    path('excluir/<int:id_tipo>/', views.delete_tipo, name='delete_tipo'),
]