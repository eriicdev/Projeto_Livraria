# 📚 bookstore-02

Aplicação de uma loja fictícia desenvolvida com o objetivo de aprendizagem do framework `Django Rest Framework`.

---

## ✅ Requisitos da Aplicação

1. A aplicação é gerenciada pelo **Poetry**
2. Utiliza **Django Rest Framework**
3. Utiliza **pytest** para testes dos `ViewSets` e `Serializers`
4. Modelos implementados:
    - **User** (modelo nativo do Django)
    - **Category**
        ```python
        from django.db import models

        class Category(models.Model):
            title = models.CharField(max_length=255)
            slug = models.SlugField(unique=True)
            description = models.TextField(max_length=500, blank=True, null=True)
            active = models.BooleanField(default=True)

            def __str__(self):
                return self.title
        ```
    - **Product**
        ```python
        from django.db import models

        class Product(models.Model):
            title = models.CharField(max_length=255)
            description = models.TextField(max_length=500, blank=True, null=True)
            price = models.DecimalField(max_digits=10, decimal_places=2)
            active = models.BooleanField(default=True)
            categories = models.ManyToManyField('Category', blank=True)
        ```
    - **Order**
        ```python
        from django.db import models
        from django.contrib.auth.models import User

        class Order(models.Model):
            products = models.ManyToManyField('product.Product', blank=False)
            user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
        ```

---

## 🔁 Rotas da API


| Rota                           | Método     | Descrição                                                                                                              |
| ------------------------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| `/bookstore/product/products/` | GET / POST | Lista e cria produtos. Filtros disponíveis via query params:<br> - `active=true/false`<br> - `category=<id_categoria>` |
| `/bookstore/product/category/` | GET / POST | Lista e cria categorias. Filtro disponivel via query params:<br> - `active=true/false`                                 |
| `/bookstore/order/order/`      | GET / POST | Lista e cria ordens de compra                                                                                          |
                                                                                     |




> ❗ As rotas aceitam os métodos `GET` e `POST` usando Django Rest Framework.

---

## 🧪 Testes Automatizados

- Todos os **ViewSets** e **Serializers** devem conter testes com **pytest**.
- Os testes devem cobrir os principais fluxos de criação, listagem e validação dos modelos.

---

## ⚙️ Requisitos de Sistema

- Python 3.10+
- Poetry (https://python-poetry.org/)

---

## ▶️ Como executar o projeto

1. Instale as dependências do projeto:

```bash
poetry install
```

2. Aplique as migrações:

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

3. Inicie o servidor local:

```bash
poetry run python manage.py runserver
```

4. Acesse em:

```
http://localhost:8000/
```

---

## 📌 Observações

- Projeto ideal para treinar conceitos de APIs RESTful com Django.
- Está estruturado para escalar com versionamento de API (`v1`, `v2`).
- A autenticação e permissões podem ser adicionadas em versões futuras.

---

## 📂 Organização do Projeto

```
bookstore-02/
├── product/
│   ├── models.py
│   ├── serializers.py
│   └── views.py
├── order/
│   ├── models.py
│   ├── serializers.py
│   └── views.py
├── tests/
│   ├── test_products.py
│   └── test_orders.py
├── manage.py
└── pyproject.toml
```

---

## ✍️ Autor

Anderson Costa – [GitHub](https://github.com/AndersonCostaDev01)

## 🐋 Projeto "Docker"

para criar a `Imagem` do docker rode

```bash
docker build -t <nome-do-docker> .
```

agora para rodar 

```bash
docker run --name <nome-da-aplicação> --rm -d -p 8000:8000 <nome-do-docker>:<tag>
``` 

link para ver esta imagem docker

DockerHub - [Imagens](https://hub.docker.com/r/costaandersom/bookstore/tags)

Para executar lembre de ter o Docker em sua maquina [Docker - Dowload](https://www.docker.com/) 

rode no terminal 
```bash
docker run --name bookstore --rm -d -p 8000:8000 costaandersom/bookstore:0.0.1
``` 
ele vai rodar internamente em sua maquina na porta `localhost:8000`

## 🦑 Docker Compose

Apos a imagem pronta para subir o docker compose use 

```bash
docker compose up --build
```

ele ira buildar a imagem e subir o container 

apos subir tudo e nessesario rodas as migraçoes no db  então rode no terminal na pasta do `docker-compose.yml`

```bash
docker compose exec web poetry run python manage.py migrate
```

com isso sua aplicação deve esta de pe e rodando normalemente na porta `8000` de sua maquina 