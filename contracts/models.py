from django.db import models


class Contract(models.Model):
    CONTRACT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('terminated', 'Terminated'),
    ]

    contract_number = models.CharField(max_length=20, unique=True)
    client_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=CONTRACT_STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.contract_number} - {self.client_name}"

    class Meta:
        ordering = ['start_date']
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'