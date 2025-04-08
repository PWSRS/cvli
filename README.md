# Iniciar o projeto Django

python -m venv venv
. venv/bin/activate (no MAC)
. \venv\scripts\activate (ativa o ambiente virutal)
pip install django
django-admin startproject project .
python manage.py startapp contact (cria o App Contact)
# após isso copiar o nome do App criado e colocar no settings dentro do projeto e colcar em INSTALLED_APPS

# Configurar o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore
git init
git add . (esse comando adiciona um arquivo no Git)
git commit -m 'Mensagem' (normalmente a primeira mensagem é Initial)
git remote add origin URL_DO_GIT (ver vídeo expplicativo)

# Migrando a base de dados do Django
python manage.py migrate (cria as tabelas da base de dados, admin, etc)
python manage.py makemigrations


# Criando e modificando a senha de um super usuário Django
python manage.py createsuperuser
python manage.py changepassword USERNAME (quando esquecer a senha do usuário)

# Trabalhando com o model do Django

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
