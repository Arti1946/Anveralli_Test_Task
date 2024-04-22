from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "pub_date",
        "title",
        "price",
        "description",
        "customer",
        "executor",
    )
    search_fields = ("title",)
    list_filter = ("customer", "pub_date", "price")
    list_editable = ("title", "price", "description", "customer", "executor")

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related("executor", "customer")
        )
