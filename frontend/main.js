fetch('http://localhost:8000/bookstore/v1/product/products/')
  .then(response => response.json())
  .then(data => {
    const appDiv = document.getElementById('app');
    console.log(data);
    const products = data.results; // pegar o array dentro de results

    if (!products || products.length === 0) {
      appDiv.innerText = 'Nenhum produto encontrado';
      return;
    }

    const ul = document.createElement('ul');
    ul.className = 'product-list';

    products.forEach(product => {
      const li = document.createElement('li');
      li.innerHTML = `
      <p>${product.title}</p>
      <p>${product.price}</p>
      <p>${product.description}</p>
      `;
      ul.appendChild(li);
    });

    appDiv.appendChild(ul);
  })
  .catch(error => {
    console.error('Erro ao buscar produtos:', error);
    document.getElementById('app').innerText = 'Erro ao carregar produtos';
  });


  // Função que cria o input com os atributos passados
function createInput(type, name, placeholder, required = false) {
  const input = document.createElement('input');
  input.type = type;
  input.name = name;
  input.placeholder = placeholder;
  if (required) input.required = true;
  return input;
}

// Criar textarea
function createTextarea(name, placeholder) {
  const textarea = document.createElement('textarea');
  textarea.name = name;
  textarea.placeholder = placeholder;
  return textarea;
}

// Criar checkbox com label
function createCheckbox(name, labelText, checked = false) {
  const label = document.createElement('label');
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.name = name;
  checkbox.checked = checked;
  label.appendChild(checkbox);
  label.appendChild(document.createTextNode(' ' + labelText));
  return label;
}

// Criar o formulário e montar tudo
function createForm() {
  const form = document.createElement('form');
  form.id = 'product-form';
  form.className = 'product-form';

  form.appendChild(createInput('text', 'title', 'Título', true));
  form.appendChild(createInput('text', 'slug', 'Slug', true));
  form.appendChild(createInput('decimal', 'price', 'Preço', true));
  form.appendChild(createInput('text', 'categories', 'Categorias (IDs separados por vírgula)'));
  form.appendChild(createTextarea('description', 'Descrição'));
  form.appendChild(createCheckbox('active', 'Ativo', true));

  const submitBtn = document.createElement('button');
  submitBtn.type = 'submit';
  submitBtn.textContent = 'Criar Produto';
  form.appendChild(submitBtn);

  // Mensagem de feedback
  const messageDiv = document.createElement('div');
  messageDiv.id = 'message';

  // Adicionar o formulário e a mensagem ao body ou a um container específico
  document.body.appendChild(form);
  document.body.appendChild(messageDiv);

  // Evento submit
  form.addEventListener('submit', function(e) {
    e.preventDefault();

    const novoProduto = {
      title: form.title.value,
      slug: form.slug.value,
      description: form.description.value,
      price: form.price.value,
      active: form.active.checked,
      categories: form.categories.value
        ? form.categories.value.split(',').map(id => parseInt(id.trim()))
        : []
    };

    fetch('http://localhost:8000/bookstore/v1/product/products/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(novoProduto)
    })
    .then(response => {
      if (!response.ok) throw new Error('Erro: ' + response.status);
      return response.json();
    })
    .then(data => {
      messageDiv.innerText = 'Produto criado com sucesso!';
      form.reset();
      console.log('Produto criado:', data);
    })
    .catch(err => {
      messageDiv.innerText = 'Erro ao criar produto';
      console.error(err);
    });
  });
}

// Executa a função para criar o formulário na página
createForm();
