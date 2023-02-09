# Cnab Reader

É um visualizador de arquivos no padrão cnab, através de parseamento a aplicação retorna uma tabela com as transações completas.
Foi desenvolvido utilizando apenas Django-Rest-Framework 

## Iniciando o projeto

**Atenção** é necessário utilizar um `ambiente virtual` para instalar as dependências.

Criando o ambiente virtual
```
python -m venv venv
```

Ativando o ambiente virtual

No linux
```
source venv/bin/activate
```
No windows 
```
.\venv\Scripts\activate
```
Instalando as dependências do projeto
```
pip install -r requirements.txt
```

Rodando as migrações

```
python manage.py makemigrations

python manage.py migrate
```

Incializando o servidor local
```
python manage.py runserver
```

## Para fazer o envio de um arquivo:
Acesse
```
http://127.0.0.1:8000/api/
```
Envie o arquivo de texto, após a pagina recarregar acesse o link abaixo para vizualizar a tabela
```
http://127.0.0.1:8000/api/table/
```
