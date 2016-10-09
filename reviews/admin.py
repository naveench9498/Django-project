from django.contrib import admin

from .models import Car, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('car', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Car)
admin.site.register(Review, ReviewAdmin)
