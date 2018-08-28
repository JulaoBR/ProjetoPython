from django.contrib import admin
from .models import Funcionario
from .models import Produto
from .models import Fornecedor
from .models import Empresa
from .models import UnidadeMedida
from .models import Grupo

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Produto)
admin.site.register(Fornecedor)
admin.site.register(UnidadeMedida)
admin.site.register(Empresa)
admin.site.register(Grupo)