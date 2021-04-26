from django.contrib import admin
from .models import Product
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sales_order_no', 'customer_name', 'item_code', 'item_cod_desc', 'exp_date_f', 'qty', 'comments', 'status', 'profile')
    list_filter = ("active",)
    search_fields = ("sales_order_no", "customer_name", )

    # def view_profile(self, obj):
    #     url = reverse("admin:live_profile_change", args=[obj.profile.id])
    #     return format_html('<a href="{}">{}</a>', url, obj.profile.item_code)
    
    #view_profile.short_description = "ITEM CODE"  
    
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'detail', 'date', 'status')

# class LogAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product_id', 'status_id')

# class StatusAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description')

# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status')

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('item_code', 'item_cod_desc', 'name', 'link', 'level')

# class Prof_Loc_Admin(admin.ModelAdmin):
#     list_display = ('id', 'profile_id', 'location_id', 'step')

# class Location_User_Admin(admin.ModelAdmin):
#      list_display = ('location_id', 'user_id')


##### Register your models here.
admin.site.register(Product, ProductAdmin)
# admin.site.register(Comment, CommentAdmin)
# admin.site.register(Log, LogAdmin)
# admin.site.register(Status, StatusAdmin)
# admin.site.register(Location, LocationAdmin)
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Profile_Location, Prof_Loc_Admin)
# admin.site.register(Location_User, Location_User_Admin)
