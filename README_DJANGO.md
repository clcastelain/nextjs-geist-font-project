# Sistema Web Profissional Django

Este é um sistema web profissional desenvolvido com Django, incluindo autenticação, dashboard e múltiplas funcionalidades.

## 🚀 Funcionalidades

- **Sistema de Login/Logout** com autenticação Django
- **Dashboard Principal** com estatísticas e navegação
- **Páginas Funcionais**: Cadastros, Processos, Consultas, Relatórios, Configurações, Básico (Países, Estados, Cidades)
- **Design Responsivo** com Bootstrap 5
- **Interface Moderna** com animações e hover effects
- **Proteção de Páginas** com @login_required

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. **Clone ou extraia o projeto**
```bash
cd sistema-django
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py migrate
```

5. **Crie um superusuário (opcional)**
```bash
python manage.py createsuperuser
```

## 🚀 Executando o Projeto

1. **Inicie o servidor de desenvolvimento**
```bash
python manage.py runserver
```

2. **Acesse a aplicação**
- URL: http://localhost:8000
- Usuário: admin
- Senha: 123abc*

## 📁 Estrutura do Projeto

```
sistema-django/
├── manage.py                 # Script principal do Django
├── db.sqlite3               # Banco de dados SQLite
├── myproject/               # Configurações principais
│   ├── settings.py          # Configurações do Django
│   ├── urls.py              # URLs principais
│   └── wsgi.py              # WSGI configuration
├── accounts/                # App de autenticação
│   ├── urls.py              # URLs de login/logout
│   └── views.py             # Views de autenticação
├── dashboard/               # App principal
│   ├── urls.py              # URLs do dashboard
│   └── views.py             # Views do dashboard
├── templates/               # Templates HTML
│   ├── base.html            # Template base
│   ├── accounts/            # Templates de autenticação
│   └── dashboard/           # Templates do dashboard
└── static/                  # Arquivos estáticos
    ├── css/                 # Estilos CSS
    └── js/                  # Scripts JavaScript
```

## 🎨 Tecnologias Utilizadas

- **Backend**: Django 5.2.3
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5
- **Ícones**: Bootstrap Icons
- **Fontes**: Google Fonts (Inter)
- **Banco de Dados**: SQLite

## 🔐 Credenciais de Acesso

- **Usuário:** admin
- **Email:** claudinei@bonssens.com.br
- **Senha:** 123abc*

## 📱 Páginas Disponíveis

1. **Login** (`/accounts/login/`) - Página de autenticação
2. **Dashboard** (`/dashboard/`) - Página principal com estatísticas
3. **Cadastros** (`/dashboard/cadastros/`) - Gerenciamento de usuários
4. **Processos** (`/dashboard/processos/`) - Controle de processos
5. **Consultas** (`/dashboard/consultas/`) - Sistema de pesquisa
6. **Relatórios** (`/dashboard/relatorios/`) - Geração de relatórios
7. **Configurações** (`/dashboard/configuracoes/`) - Configurações do sistema
8. **Básico** (`/dashboard/basico/paises/`) - Gestão de Países, Estados e Cidades com busca e filtros avançados

## 🔍 Funcionalidades Avançadas de Busca e Filtros

- As páginas de Países, Estados e Cidades possuem formulários de busca e filtros avançados.
- Utilize os campos de busca para filtrar os registros exibidos.
- Botões para "Buscar" e "Limpar" facilitam a navegação.
- Paginação integrada para facilitar a visualização de grandes volumes de dados.

## 🛠️ Personalização

### Alterando Estilos
- Edite `static/css/style.css` para personalizar o visual
- Modifique `templates/base.html` para alterar a estrutura base

### Adicionando Funcionalidades
- Crie novos models em `dashboard/models.py`
- Adicione views em `dashboard/views.py`
- Configure URLs em `dashboard/urls.py`
- Crie templates em `templates/dashboard/`

### Configurações de Produção
- Altere `DEBUG = False` em `settings.py`
- Configure `ALLOWED_HOSTS` adequadamente
- Use um banco de dados mais robusto (PostgreSQL, MySQL)
- Configure arquivos estáticos para produção

## 📞 Suporte

Para dúvidas ou suporte, consulte a documentação oficial do Django:
https://docs.djangoproject.com/

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e profissionais.
