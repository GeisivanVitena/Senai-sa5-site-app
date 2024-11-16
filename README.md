Sistema web para gerenciamento de vendas

Este projeto é um sistema web desenvolvido para gerenciar as vendas de uma lanchonete. 

O sistema permite o cadastro de clientes, gerenciamento de informações, e a integração com um banco de dados MySQL. 

A aplicação foi construída utilizando Python, Django, HTML, CSS, e JavaScript.

Funcionalidades:

Cadastro de Clientes: Permite o registro de novos clientes no sistema.

Listagem de Clientes: Exibe os clientes cadastrados no banco de dados.

Pesquisa de Clientes: Permite buscar um cliente específico pelo nome.

Atualização de Dados: Permite atualizar as informações de clientes já cadastrados.

Exclusão de Clientes: Permite excluir registros de clientes do banco de dados.

Estrutura do Projeto:

atualizar.html: Página para atualização de informações no sistema.

cadastro.html: Interface para cadastrar um cliente.

contatos.html: Página de contato com informações da lanchonete.

detalhes.html: Exibe detalhes de um produto.

home.html: Página inicial do site, exibindo informações gerais.

index.html: Estrutura base principal do sistema.

pesquisar.html: Permite a pesquisa de cliente cadastrado.

produtos.html: Exibe os produtos disponíveis no sistema.

update.html: Página para atualização de dados no sistema.

Tecnologias Utilizadas:

Back-end: Python, Django

Front-end: HTML, CSS, JavaScript

Banco de Dados: MySQL

Como Rodar o Projeto:

1 - Clone o repositório:

git clone <URL_DO_REPOSITORIO>

2 - Instale as dependências:

pip install -r requirements.txt

3 - Configure o banco de dados MySQL no arquivo settings.py.

4 - Execute as migrações do banco de dados:

python manage.py migrate

5 - Inicie o servidor de desenvolvimento:

python manage.py runserver

6 - Acesse o sistema em http://127.0.0.1:8000.










