from django.db import models

class KanbanBoard(models.Model):
    name = models.CharField(max_length=255)

    def delete(self, *args, **kwargs):
        self.columns.all().delete()
        super().delete(*args, **kwargs)

class Column(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(KanbanBoard, related_name='columns', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def delete(self, *args, **kwargs):
        self.cards.all().delete()
        super().delete(*args, **kwargs)

class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    column = models.ForeignKey(Column, related_name='cards', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    data = models.JSONField(blank=True, null=True)

    def move_to_column(self, new_column, new_order):
        self.column = new_column
        self.order = new_order
        self.save()