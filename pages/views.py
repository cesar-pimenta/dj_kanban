# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from common.models import KanbanBoard, Column, Card
import json

def board_list(request):
    boards = KanbanBoard.objects.all()
    return render(request, 'pages/board_list.html', {'boards': boards})

def create_board(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        board = KanbanBoard.objects.create(name=name)
        return JsonResponse({'id': board.id, 'name': board.name})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_board(request, board_id):
    if request.method == 'DELETE':
        board = get_object_or_404(KanbanBoard, id=board_id)
        board.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def index(request, board_id):
    board = get_object_or_404(KanbanBoard, id=board_id)
    columns = board.columns.all().order_by('order')
    return render(request, 'pages/dashboard.html', {'board': board, 'columns': columns})

def add_column(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        board_id = int(data.get('board_id'))
        board = get_object_or_404(KanbanBoard, id=board_id)
        column = Column.objects.create(name=name, board=board, order=Column.objects.filter(board=board).count())
        return JsonResponse({'id': column.id, 'name': column.name})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_column(request, column_id):
    if request.method == 'DELETE':
        column = get_object_or_404(Column, id=column_id)
        column.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def add_card(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        column_id = int(data.get('column_id'))
        column = get_object_or_404(Column, id=column_id)
        card = Card.objects.create(title=title, description=description, column=column, order=column.cards.count())
        return JsonResponse({'id': card.id, 'title': card.title, 'description': card.description})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_card(request, card_id):
    if request.method == 'DELETE':
        print(request)
        print(card_id)
        card = get_object_or_404(Card, id=card_id)
        print(card)
        card.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def move_card(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_id = int(data.get('card_id'))
        new_column_id = int(data.get('new_column_id'))
        new_order = int(data.get('new_order'))
        card = get_object_or_404(Card, id=card_id)
        new_column = get_object_or_404(Column, id=new_column_id)
        card.move_to_column(new_column, new_order)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

