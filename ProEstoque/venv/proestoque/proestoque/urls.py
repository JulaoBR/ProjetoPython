from django.contrib import admin
from django.urls import path
from aplicacaoWeb.views import home
from aplicacaoWeb.views import cadProduto

app_name = 'proestoque'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('cadProduto/', cadProduto)
]
