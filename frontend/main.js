// Função para buscar e criar select múltiplo de categorias
async function createSelectMultiple(name, url) {
  const select = document.createElement('select');
  select.name = name;
  select.id = name;
  select.multiple = true;
  select.size = 5;

  try {
    const response = await fetch(url);
    const data = await response.json();

    data.results.forEach(category => {
      const option = document.createElement('option');
      option.value = category.id;
      option.textContent = category.title;
      select.appendChild(option);
    });
  } catch (error) {
    console.error('Erro ao carregar categorias:', error);
    const option = document.createElement('option');
    option.textContent = 'Erro ao carregar categorias';
    option.disabled = true;
    select.appendChild(option);
  }

  return select;
}

// Cria input
function createInput(type, name, placeholder, required = false) {
  const input = document.createElement('input');
  input.type = type;
  input.name = name;
  input.placeholder = placeholder;
  if (required) input.required = true;
  return input;
}

// Cria textarea
function createTextarea(name, placeholder) {
  const textarea = document.createElement('textarea');
  textarea.name = name;
  textarea.placeholder = placeholder;
  return textarea;
}

// Cria checkbox
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

// Cria formulário principal
async function createForm() {
  const form = document.createElement('form');
  form.id = 'product-form';
  form.className = 'product-form';

  form.appendChild(createInput('text', 'title', 'Título', true));
  form.appendChild(createInput('text', 'slug', 'Slug', true));
  form.appendChild(createInput('decimal', 'price', 'Preço', true));

  // Substitui input de categorias por select múltiplo
  const label = document.createElement('label');
  label.htmlFor = 'categories';
  label.textContent = 'Categorias (Selecione múltiplas)';
  form.appendChild(label);
  const selectCategories = await createSelectMultiple(
    'categories',
    'http://localhost:8000/bookstore/v1/product/category/'
  );
  form.appendChild(selectCategories);

  form.appendChild(createTextarea('description', 'Descrição'));
  form.appendChild(createCheckbox('active', 'Ativo', true));

  const submitBtn = document.createElement('button');
  submitBtn.type = 'submit';
  submitBtn.textContent = 'Criar Produto';
  form.appendChild(submitBtn);

  const messageDiv = document.createElement('div');
  messageDiv.id = 'message';

  document.body.appendChild(form);
  document.body.appendChild(messageDiv);

  // SUBMIT
  form.addEventListener('submit', function(e) {
    e.preventDefault();

    // Pega os valores selecionados no select múltiplo
    const selectedCategories = Array.from(selectCategories.selectedOptions).map(opt => parseInt(opt.value));

    const novoProduto = {
      title: form.title.value,
      slug: form.slug.value,
      description: form.description.value,
      price: form.price.value,
      active: form.active.checked,
      categories: selectedCategories
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

// Executa o formulário
createForm();

// Exibe lista de produtos existentes
fetch('http://localhost:8000/bookstore/v1/product/products/')
  .then(response => response.json())
  .then(data => {
    const appDiv = document.getElementById('app');
    console.log(data);
    const products = data.results;

    if (!products || products.length === 0) {
      appDiv.innerText = 'Nenhum produto encontrado';
      return;
    }

    const ul = document.createElement('ul');
    ul.className = 'product-list';

    products.forEach(product => {
      const li = document.createElement('li');
      li.innerHTML = `
        <p><strong>${product.title}</strong></p>
        <p>R$ ${product.price}</p>
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
