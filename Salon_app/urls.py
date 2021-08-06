from Salon_app import views
from django.urls import path, include
from django.views.generic.base import TemplateView



urlpatterns = [
    path('cd/', views.cd_list),
    path('sells/', views.sell_list),
    path('topchart/', views.topchart),
    path('cd/cds/<int:pollid>/', views.buysucc),
    path('cd/cdinfo/<int:pollid>/', views.cdinfo),
    path('register/', views.RegisterFormView.as_view()),
    path('arrivals/', views.arr_list),
    path('tracks/', views.track_list),
    path('addcd/', views.create_cdview),
    path('addcdalbum/', views.create_cdalbumview),
    path('addarrival/', views.create_arrview),
    path('addalbum/', views.create_albumview),
    path('addtrack/', views.create_trackview),
    path('succ/', TemplateView.as_view(template_name="succ.html")),

]