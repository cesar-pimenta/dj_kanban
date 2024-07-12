from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_number', 'client_name', 'start_date', 'end_date', 'contract_amount', 'status')
    search_fields = ('contract_number', 'client_name')
    list_filter = ('status', 'start_date', 'end_date')
    ordering = ('start_date',)
    fields = (
        'contract_number',
        'client_name',
        'start_date',
        'end_date',
        'contract_amount',
        'status',
        'description',
    )
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Contract, ContractAdmin)
