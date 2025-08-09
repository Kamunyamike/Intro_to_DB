from django.contrib import admin
from .models import Book

@admin.action(description='Apply 10%% discount')
def apply_discount(modeladmin, request, queryset):
    for book in queryset:
        book.price *= 0.9
        book.save()

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    search_fields = ('title', 'author')
    list_filter = ('author',)
    list_editable = ('price',)
    ordering = ('title',)
    actions = [apply_discount]
    # Optional field grouping
    fieldsets = (
        ('Book Info', {'fields': ('title', 'author')}),
        ('Financials', {'fields': ('price',)}),
    )

admin.site.register(Book, BookAdmin)