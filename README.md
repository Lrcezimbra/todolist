## Como desenvolver

1. Clone o repositório
2. Crie um virtualenv com o Python 3
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:Lrcezimbra/todolist.git todolist
cd todolist
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como rodar o projeto

1. Executar os passos do Como desenvolver 
2. Rodar as migrações
3. Rodar o servidor

```console
python manage.py migrate
python manage.py runserver
```

## Como fazer o deploy

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Envie o código para o Heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`SECRETA_SEGURA`
heroku config:set DEBUG=False
git push --force heroku maste
```
