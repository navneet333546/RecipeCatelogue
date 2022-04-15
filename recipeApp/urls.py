from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URLConf
urlpatterns = [
    path("",views.say_hello),
    path('recipes/',views.show_recipes),
    path('recipeDetails',views.show_recipeDetails),
    path('dataModel',views.show_dataModel),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)