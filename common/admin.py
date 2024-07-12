from django.contrib import admin
from .models import KanbanBoard, Column, Card

class ColumnInline(admin.TabularInline):
    model = Column
    extra = 1

class CardInline(admin.TabularInline):
    model = Card
    extra = 1

@admin.register(KanbanBoard)
class KanbanBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [ColumnInline]

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'board', 'order')
    list_filter = ('board',)
    inlines = [CardInline]

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'column', 'order')
    list_filter = ('column',)
    search_fields = ('title', 'description')