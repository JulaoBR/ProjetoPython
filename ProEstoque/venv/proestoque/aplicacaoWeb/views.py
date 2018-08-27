from django.shortcuts import render

# Create your views here.
def IndexTemplateView(request):
   
   return render(request, "aplicacaoWeb/index.html")

def cadProduto(request):

    return render(request, 'aplicacaoWeb/cadProduto.html')   