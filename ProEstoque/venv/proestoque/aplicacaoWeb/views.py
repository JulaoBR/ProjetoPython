from django.shortcuts import render
from .models import Produto

# Create your views here.
def IndexTemplateView(request):
   
   return render(request, "aplicacaoWeb/index.html")


def Produtos(request):
    data = {}
    data['produtos'] = Produto.objects.all()
    return render(request, 'aplicacaoWeb/produtos.html', data)   

