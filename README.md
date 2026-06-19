## Integrantes da equipe
* **Alexsandro Oliveira**
* **Mateus Santanna**
* **Pedro Henri**
* **Thiago Chagas**

## Situação-Problema Escolhida
**Circuito Saquarema Verde**: O projeto tem como foco o ecoturismo na região de Saquarema, especificamente promovendo o acesso à informação sobre o Parque Estadual da Costa do Sol e a Reserva Ecológica Estadual de Jacarepiá.

## Descrição do MVP
Este projeto é o Back-End (API RESTful) da plataforma "Saquarema Verde Online". O sistema visa centralizar informações relevantes sobre atrações naturais, simplificando a consulta sobre a biodiversidade, trilhas, cachoeiras e eventos locais para os turistas e moradores. O servidor fornece os dados em formato JSON para serem consumidos pelo Front-End, garantindo respostas rápidas, persistência de dados e segurança para os administradores.

### Tecnologias Utilizadas
* **Linguagem:** Python
* **Framework:** Django (Padrão MTV) e Django REST Framework
* **Banco de Dados:** MongoDB (NoSQL) integrado via Djongo

## Funcionalidades da API
* Listagem pública de eventos ativos e informações dos parques.
* Autenticação segura para acesso à área administrativa.
* Gerenciamento completo (CRUD - Criar, Ler, Atualizar e Excluir) de eventos, trilhas e atividades ao ar livre exclusivo para administradores logados.

## Instruções de Instalação e Execução Local

Siga os passos abaixo para configurar o ambiente de desenvolvimento na sua máquina:

**1. Clone o repositório**
git clone https://github.com/MateusSantanna/mvp-back-end.git
cd mvp-back-end

**2. Crie e ative um ambiente virtual**
python -m virtualenv venv
### No Windows:
venv\Scripts\activate
### No Linux/Mac:
source venv/bin/activate

**3. Instale as dependências**
pip install -r requirements.txt

**4. Configure o banco de dados MongoDB**
Certifique-se de ter o MongoDB Community Server rodando na sua máquina local ou configure a URI do banco no arquivo settings.py.

**5. Execute as migrações**
python manage.py makemigrations
python manage.py migrate

**6. Inicie o servidor de desenvolvimento**
python manage.py runserver
A API estará disponível para testes e acesso através de http://127.0.0.1:8000/api/
