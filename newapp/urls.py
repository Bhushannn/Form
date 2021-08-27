
from django.urls import path,include
from . import views


urlpatterns = [
   # path('admin/', admin.site.urls),
   # path('', include('newapp.urls'),)
   path('', views.index,name='index'),
]