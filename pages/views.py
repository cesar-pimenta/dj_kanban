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
        is_movable = data.get('is_movable', True)
        board = get_object_or_404(KanbanBoard, id=board_id)
        column = Column.objects.create(name=name, board=board, order=Column.objects.filter(board=board).count(), is_movable=is_movable)
        return JsonResponse({'id': column.id, 'name': column.name, 'is_movable': column.is_movable})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def move_column(request):
    data = json.loads(request.body)
    column_order = data.get('column_order', [])

    for column_data in column_order:
        column = get_object_or_404(Column, id=column_data['id'])
        column.order = column_data['order']
        column.save()

    return JsonResponse({'status': 'success'})


def delete_column(request, column_id):
    if request.method == 'DELETE':
        column = get_object_or_404(Column, id=column_id)
        if column.is_movable:
            column.delete()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Cannot delete this column.'})
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
        card = get_object_or_404(Card, id=card_id)
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
        card.column = new_column
        card.order = new_order
        card.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

