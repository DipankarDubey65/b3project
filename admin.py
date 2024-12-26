from django.contrib import admin
from .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ("Name","Mobile","Email","Message")
admin.site.register(contactus,contactusAdmin)


class igalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gname','gpic')
admin.site.register(igallery,igalleryAdmin)


class sliderAdmin(admin.ModelAdmin):
    list_display = ( 'id','shead','ssubject','sdes','spic')
admin.site.register(slider,sliderAdmin)

##############################################
class ncategoryAdmin(admin.ModelAdmin):

    list_display=('id','category','cpic','cdate')
admin.site.register(ncategory,ncategoryAdmin)
####################################################

class cityAdimn(admin.ModelAdmin):
    list_display=('id','ncity','cpic','cdate')
admin.site.register(city,cityAdimn)

#####################################################

class mynewsAdmin(admin.ModelAdmin):
    list_display = ('id','ntitle','nhead','ndes','npic','ncity','category','ndate')

admin.site.register(mynews,mynewsAdmin)

########################################################################################

class videonewsAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vhead','vcategory','vcity','vdate','vdes')
admin.site.register(videonews,videonewsAdmin)

