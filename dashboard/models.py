from django.db import models
from django.contrib.auth.models import User

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

class Clientes(models.Model):
    idcliente = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    nome_cliente = models.CharField(max_length=60, default='', verbose_name='Nome')  # Name of the client
    insituacao = models.BooleanField(default=True, verbose_name='Ativo')   # Status of the client
    nrcpf = models.CharField(max_length=11, null=True, blank=True, verbose_name='CPF')  # CPF number
    nrrg = models.CharField(max_length=10, null=True, blank=True, verbose_name='Registro Geral')  # RG number
    nrhabilitacao = models.CharField(max_length=15, null=True, blank=True, verbose_name='Habilitação')  # License number
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data Nascimento")  # Last alteration date    
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name="Email")  # Email address
    telefone_comercial = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone")  # Commercial phone
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name="Celular")  # Cell phone
    observacao = models.TextField(null=True, blank=True, verbose_name="Observação")  # Observations
    cep = models.CharField(max_length=8, null=True, blank=True, verbose_name="CEP")  # ZIP code
    endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name='Logradouro')  # Address
    numero = models.CharField(max_length=10, null=True, blank=True, verbose_name='Número')  # Address number
    complemento = models.CharField(max_length=250, null=True, blank=True, verbose_name='Complemento')  # Address complement
    bairro = models.CharField(max_length=50, null=True, blank=True, verbose_name='Bairro') # Address complement# Neighborhood
    idcidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")  # Foreign key to Cidade
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, verbose_name="Data ult. alteração")  # Last alteration date
    nacionalidade = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nacionalidade")  # Nationality
    naturalidade = models.CharField(max_length=60, null=True, blank=True, verbose_name="Naturalidade") #  # Naturalness
    nome_mae = models.CharField(max_length=60, null=True, blank=True, verbose_name="Nome da mãe")  # Mother's name
    nome_pai = models.CharField(max_length=60, null=True, blank=True, verbose_name="Nome do pai")  # Father's name
    profissao = models.CharField(max_length=60, null=True, blank=True, verbose_name='Profissão')  # Profession
    idestadocivil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, verbose_name='Estado Civíl')  # Marital status

    class Meta:
        db_table = 'clientes'  # Specify the database table name
        unique_together = (('nrcpf'),)  # Unique constraint
        managed = True  # Django will manage the table


    def __str__(self):
        return self.nome_cliente

    def clean(self):
        super().clean()
        if self.nrcpf:
            self.validate_cpf(self.nrcpf)

    def validate_cpf(self, cpf):
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', cpf)

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            raise ValidationError(_('O CPF deve ter 11 dígitos.'))

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * len(cpf):
            raise ValidationError(_('O CPF não pode ter todos os dígitos iguais.'))
        
        if not cpfcnpj.validate(cpf):
            raise ValidationError(_('O CPF invalido.'))  