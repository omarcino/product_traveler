from django.contrib import admin
from .models import Product, Location, Profile, Comment, Status, Log, Profile_Location, Location_User

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'item_code', 'item_cod_desc')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'detail', 'date', 'status')

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'status_id')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'item_code', 'item_cod_desc')

class Prof_Loc_Admin(admin.ModelAdmin):
    list_display = ('id', 'profile_id', 'location_id', 'step')

class Location_User_Admin(admin.ModelAdmin):
     list_display = ('id', 'location_id', 'user_id')


##### Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile_Location, Prof_Loc_Admin)
admin.site.register(Location_User, Location_User_Admin)
