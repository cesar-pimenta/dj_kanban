from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    # Boards
    path('create_board/', views.create_board, name='create_board'),
    path('delete_board/<int:board_id>/', views.delete_board, name='delete_board'),
    path('board/<int:board_id>/', views.index, name='index'),
    # Colunas
    path('add_column/', views.add_column, name='add_column'),
    path('move_column/', views.move_column, name='update_column_order'),
    path('delete_column/<int:column_id>/', views.delete_column, name='delete_column'),
    # Cards
    path('add_card/', views.add_card, name='add_card'),
    path('move_card/', views.move_card, name='move_card'),
    path('delete_card/<int:card_id>/', views.delete_card, name='delete_card'),
]