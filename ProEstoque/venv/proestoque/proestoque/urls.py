from django.contrib import admin
from django.urls import path
from aplicacaoWeb.views import IndexTemplateView, Produtos

app_name = 'proestoque'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView),
    path('produtos/', Produtos )
]
