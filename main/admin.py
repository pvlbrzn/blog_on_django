import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from .models import Post, Movie

admin.site.register(Post)


# Экспорт фильмов в CSV
@admin.action(description='Экспорт выбранных фильмов в CSV')
def export_movies_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    # Настраиваем HTTP-ответ с типом CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)

    # Записываем заголовок CSV
    writer.writerow(field_names)
    # Записываем данные по каждой выбранной записи
    for obj in queryset:
        row = [getattr(obj, field) for field in field_names]
        writer.writerow(row)
    return response


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'styled_price')  # Заменяем price на styled_price
    search_fields = ('name', 'price')
    list_filter = ('price',)
    actions = [export_movies_csv]

    class Media:
        css = {
            "all": ("admin/css/admin_custom.css",)
        }

    # Делаем цену стилизованной
    def styled_price(self, obj):
        return format_html('<span style="color: green; font-weight: bold;">{} руб.</span>', obj.price)

    styled_price.short_description = "Цена"


admin.site.register(Movie, MovieAdmin)
