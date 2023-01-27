from django.contrib import admin
from .models import Order, Comment

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass