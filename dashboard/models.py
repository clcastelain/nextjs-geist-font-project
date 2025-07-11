from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    codigo_iso2 = models.CharField(max_length=2, unique=True, verbose_name='Código ISO 2')
    codigo_iso3 = models.CharField(max_length=3, unique=True, verbose_name='Código ISO 3')
    ddi = models.CharField(max_length=5, verbose_name='Código DDI', help_text='Ex: +55 para Brasil')
    codigo_siscomex = models.CharField(max_length=5, unique=True, verbose_name='Código Siscomex')
    continente = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.codigo_iso2})"

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2, unique=True, verbose_name='Sigla UF')
    pais = models.ForeignKey('Pais', on_delete=models.PROTECT, related_name='estados')
    codigo_ibge = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name='Código IBGE',
        help_text='Código oficial do estado'
    )
    regiao = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Região',
        help_text='Ex: Sudeste, Nordeste, etc.'
    )

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        unique_together = ('nome', 'pais')
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.sigla})"

class Cidade(models.Model):
    nome = models.CharField(max_length=150)
    estado = models.ForeignKey('Estado', on_delete=models.PROTECT, related_name='cidades')
    codigo_ibge = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Código IBGE',
        help_text='Código oficial da cidade, se aplicável'
    )
    cep = models.CharField(
        max_length=9,
        blank=True,
        null=True,
        verbose_name='CEP Inicial',
        help_text='Faixa de CEP (se houver)'
    )

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        unique_together = ('nome', 'estado')  # Evita cidades duplicadas no mesmo estado
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} / {self.estado.sigla}"

class Empresa(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    site = models.URLField(blank=True, null=True)
    data_fundacao = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class EstadoCivil(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civis'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Escolaridade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridades'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Objetivo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Objetivo'
        verbose_name_plural = 'Objetivos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class BeneficioINSS(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    descricao = models.TextField(blank=True, null=True)


    class Meta:
        verbose_name = 'Benefício INSS'
        verbose_name_plural = 'Benefícios INSS'
        ordering = ['nome']

    def __str__(self):
        return self.nome
