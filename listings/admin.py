from django.contrib import admin

from  .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'titile', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'titile')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('titile', 'description', 'address', 'city', 'state','zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
