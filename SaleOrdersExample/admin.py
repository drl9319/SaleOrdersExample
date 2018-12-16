from django.contrib import admin

from .models import Client, Product, SaleOrder, SaleOrderLine


class SaleLine(admin.TabularInline):
    model = SaleOrderLine
    extra = 2


class SaleOrderAdmin(admin.ModelAdmin):
    fieldsets = [
        #(None,               {'fields': ['question_text']}),
        ('Sale information',
            {
                'fields': ['IdClient', 'Date'],
                'classes': ['Date']
            }
        ),
    ]
    inlines = [SaleLine]

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(SaleOrder, SaleOrderAdmin)
#admin.site.register(SaleOrder)
#admin.site.register(SaleOrderAdmin)
