from django.contrib import admin
from .models import Funcionario
from .models import Produto
from .models import Fornecedor

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Produto)
admin.site.register(Fornecedor)