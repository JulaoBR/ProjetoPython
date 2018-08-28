from django.db import models

# MODELO DE FUNCIONARIO
# ------------------------------------------
class Funcionario(models.Model):

    fun_nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.fun_nome

# MODELO DE EMPRESA
# ------------------------------------------
class Empresa(models.Model):

    emp_razao_social = models.CharField(
        max_length = 150,
        null = False,
        blank = False
    )

    emp_nome_fantasia = models.CharField(
        max_length = 150,
        null = False,
        blank = False
    )

    emp_endereco = models.CharField(
        max_length = 150,
        null = False,
        blank = False
    )

    emp_numero = models.CharField(
        max_length = 5,
        null = False,
        blank = False
    )

    emp_bairro = models.CharField(
        max_length = 150,
        null = False,
        blank = False
    )

    emp_cidade = models.CharField(
        max_length = 150,
        null = False,
        blank = False
    )

    emp_cep = models.CharField(
        max_length = 8,
        null = False,
        blank = False
    )

    emp_cnpj_cpf =models.CharField(
        max_length = 12,
        null = False,
        blank = False
    )

    emp_telefone = models.CharField(
        max_length = 12,
        null = False,
        blank = False
    )

    emp_celular = models.CharField(
        max_length = 12,
        null = False,
        blank = False
    )


# MODELO DE PRODUTO
# ------------------------------------------
class Produto(models.Model):

    pro_descricao = models.CharField(
       max_length=100,
       null=False,
       blank=False 
    )

    pro_qtd_minima = models.DecimalField(
        default = 0,
        max_digits = 8,
        decimal_places = 3,
        null=False,
        blank=False 
    )

    pro_qtd_maxima = models.DecimalField(
        default = 0,
        max_digits = 8,
        decimal_places = 3,
        null = False,
        blank = False
    )

    pro_prazo_validade = models.IntegerField(
        default = 0,
        null = False,
        blank = False
    )

    pro_peso_liquido = models.DecimalField(
        default = 0,
        max_digits = 8,
        decimal_places = 3,
        null = False,
        blank = False
    )

    pro_peso_bruto = models.DecimalField(
        default = 0,
        max_digits = 8,
        decimal_places = 3,
        null = False,
        blank = False
    )

    grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE, null=True)
    unidade = models.ForeignKey('UnidadeMedida', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pro_descricao


# MODELO DE FORNECEDOR
# ------------------------------------------
class Fornecedor(models.Model):

    for_descricao = models.CharField(
       max_length=100,
       null=False,
       blank=False 
    )

    def __str__(self):
        return self.for_descricao

# MODELO DE CATEGORIA
# ------------------------------------------
class Grupo(models.Model):

    gru_descricao = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )

    def __str__(self):
        return self.gru_descricao


# MODELO DE UNIDADE MEDIDA
# ------------------------------------------
class UnidadeMedida(models.Model):

    uni_descricao = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )

    uni_sigla = models.CharField(
        max_length = 2,
        null = False,
        blank = False
    )

    def __str__(self):
        return self.uni_descricao

'''
    class Teste(models.Model):
        //campo data decimal
        valor = models.DecimalField(max_digits=7, decimal_places=2)

        //faz relacionamento entre tabelas
        categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE),

        class Metsa:
            varbose_name_plural = 'Transações'
'''