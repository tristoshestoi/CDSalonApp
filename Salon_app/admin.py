from django.contrib import admin
from Salon_app.models import CD
from Salon_app.models import Album
from Salon_app.models import Track
from Salon_app.models import CdHasAlbum
from Salon_app.models import SellArrival
from Salon_app.models import company_maker

admin.site.register(CD)
admin.site.register(Album)
admin.site.register(CdHasAlbum)
admin.site.register(SellArrival)
admin.site.register(Track)
admin.site.register(company_maker)


# Register your models here.
