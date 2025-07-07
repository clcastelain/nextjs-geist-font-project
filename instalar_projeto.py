#!/usr/bin/env python3
"""
Script de instalação automática do Sistema Django
Execute este script para configurar automaticamente o projeto
"""

import os
import sys
import subprocess
import platform

def executar_comando(comando, descricao):
    """Executa um comando e exibe o resultado"""
    print(f"\n🔄 {descricao}...")
    try:
        resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {descricao} - Concluído!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro em {descricao}: {e}")
        print(f"Saída do erro: {e.stderr}")
        return False

def verificar_python():
    """Verifica se o Python está instalado"""
    versao = sys.version_info
    if versao.major >= 3 and versao.minor >= 8:
        print(f"✅ Python {versao.major}.{versao.minor}.{versao.micro} encontrado")
        return True
    else:
        print(f"❌ Python 3.8+ é necessário. Versão atual: {versao.major}.{versao.minor}.{versao.micro}")
        return False

def main():
    print("🚀 INSTALADOR DO SISTEMA DJANGO")
    print("=" * 50)
    
    # Verificar Python
    if not verificar_python():
        sys.exit(1)
    
    # Verificar se está no diretório correto
    if not os.path.exists('manage.py'):
        print("❌ Arquivo manage.py não encontrado!")
        print("Execute este script no diretório raiz do projeto Django")
        sys.exit(1)
    
    print("\n📦 Iniciando instalação...")
    
    # Instalar dependências
    if not executar_comando("pip install -r requirements.txt", "Instalando dependências"):
        print("⚠️  Tentando com pip3...")
        if not executar_comando("pip3 install -r requirements.txt", "Instalando dependências com pip3"):
            print("❌ Falha na instalação das dependências")
            sys.exit(1)
    
    # Executar migrações
    if not executar_comando("python manage.py migrate", "Executando migrações do banco de dados"):
        print("⚠️  Tentando com python3...")
        if not executar_comando("python3 manage.py migrate", "Executando migrações com python3"):
            print("❌ Falha nas migrações")
            sys.exit(1)
    
    # Criar superusuário automaticamente
    print("\n👤 Criando superusuário...")
    script_superuser = """
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'claudinei@bonssens.com.br', '123abc*')
    print('Superusuário criado com sucesso!')
else:
    print('Superusuário já existe!')
"""
    
    try:
        with open('temp_create_user.py', 'w') as f:
            f.write(script_superuser)
        
        if not executar_comando("python manage.py shell < temp_create_user.py", "Criando superusuário"):
            executar_comando("python3 manage.py shell < temp_create_user.py", "Criando superusuário com python3")
        
        os.remove('temp_create_user.py')
    except Exception as e:
        print(f"⚠️  Aviso: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 50)
    print("\n📋 INFORMAÇÕES DE ACESSO:")
    print("🌐 URL: http://localhost:8000")
    print("👤 Usuário: admin")
    print("🔑 Senha: 123abc*")
    print("📧 Email: claudinei@bonssens.com.br")
    
    print("\n🚀 PARA INICIAR O SERVIDOR:")
    if platform.system() == "Windows":
        print("   python manage.py runserver")
    else:
        print("   python3 manage.py runserver")
    
    print("\n📚 DOCUMENTAÇÃO:")
    print("   Leia o arquivo README_DJANGO.md para mais informações")
    
    # Perguntar se deseja iniciar o servidor
    resposta = input("\n❓ Deseja iniciar o servidor agora? (s/n): ").lower().strip()
    if resposta in ['s', 'sim', 'y', 'yes']:
        print("\n🚀 Iniciando servidor...")
        try:
            if platform.system() == "Windows":
                subprocess.run("python manage.py runserver", shell=True)
            else:
                subprocess.run("python3 manage.py runserver", shell=True)
        except KeyboardInterrupt:
            print("\n👋 Servidor interrompido pelo usuário")

if __name__ == "__main__":
    main()
