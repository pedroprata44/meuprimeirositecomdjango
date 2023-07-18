# Eventex

Sistema de eventos encomendado pela Morena

## Como desenvolver

1. Clone o repositório
2. Crie um virtual com python
3. Ative seu virtual env
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```
git clone git@hub.com:pprataneto/meuprimeirositecomdjango.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
cd .wttd/Scripts>activate
pip install -r requirements.txt
cp contrib/env-sample.env
python manage.py test
```


## Como fazer o deploy

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o Heroku

```
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#configura email
git push heroku master --force
```