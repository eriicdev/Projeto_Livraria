# Criação de produtos automaticamente por codigo, fim didatico
import requests
from slugify import slugify

API_URL = "http://127.0.0.1:8000/bookstore/v1/product/products/"


def criar_produto(titulo, preco, descricao="", categorias=None):
    slug = slugify(titulo)
    data = {
        "title": titulo,
        "slug": slug,
        "price": preco,
        "description": descricao,
        "active": True,
        "categories": categorias or [1],
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        print(f"Produto '{titulo}' criado com sucesso.")
    else:
        print(f"Erro ao criar '{titulo}': {response.status_code} - {response.text}")


if __name__ == "__main__":
    for i in range(1, 101):
        titulo = f"Produto Teste {i}"
        preco = round(10 + i * 0.75, 2)
        descricao = f"Descrição do produto teste número {i}"
        categorias = [1]
        criar_produto(titulo, preco, descricao, categorias)
