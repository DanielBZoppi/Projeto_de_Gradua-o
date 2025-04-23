from django.urls import path
from wms.views import index

ap_name = 'wms'

urlpatterns = [
    path('', index, name='index'),
    path('produtos/', include('seu_app.urls')),
]


