# syntax=docker/dockerfile:1

# Usa sua imagem customizada que já tem Python 3.13 + Poetry 2.1.3 + dependências básicas
FROM costaandersom/python-poetry:3.13-slim

# Define as variáveis de ambiente específicas do projeto (opcional)
ENV PYSETUP_PATH="/opt/pysetup" \
    PATH="/opt/poetry/bin:$PATH"

# Define diretório de trabalho para instalar dependências
WORKDIR $PYSETUP_PATH

# Atualiza e instala o psycopg2
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install psycopg2

# Copia os arquivos de dependência para dentro do container
COPY poetry.lock pyproject.toml ./

# Configura o Poetry para não criar virtualenv (usar ambiente global do container)
RUN poetry config virtualenvs.create false

# Instala as dependências do projeto no ambiente global do container
RUN poetry install --no-root

# Depois muda o diretório de trabalho para o app
WORKDIR /app

# Copia o código-fonte do projeto inteiro
COPY . /app/

# Expondo a porta padrão do Django
EXPOSE 8000

# Comando default para rodar o servidor Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
