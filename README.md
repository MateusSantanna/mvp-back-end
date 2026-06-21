## Integrantes da equipe
* **Alexsandro dos Santos Oliveira**
* **Mateus Silva Santanna**
* **Pedro Henri Apolinario Gonzo**
* **Thiago Nascimento Chagas**

## Situação-Problema Escolhida
**Circuito Saquarema Verde**: O projeto tem como foco o ecoturismo na região de Saquarema, especificamente promovendo o acesso à informação sobre o Parque Estadual da Costa do Sol e a Reserva Ecológica Estadual de Jacarepiá.

## Descrição do MVP
Este projeto é o Back-End (API RESTful) da plataforma "Saquarema Verde Online". O sistema visa centralizar informações relevantes sobre atrações naturais, simplificando a consulta sobre a biodiversidade, trilhas, cachoeiras e eventos locais para os turistas e moradores. O servidor fornece os dados em formato JSON para serem consumidos pelo Front-End, garantindo respostas rápidas, persistência de dados e segurança para os administradores.

### Tecnologias Utilizadas
* **Linguagem:** Python
* **Framework:** Django (Padrão MTV) e Django REST Framework
* **Banco de Dados:** SQLite3 (Relacional Padrão do Django)

## Funcionalidades da API
* Listagem pública de eventos ativos e informações dos parques.
* Autenticação segura para acesso à área administrativa.
* Gerenciamento completo (CRUD - Criar, Ler, Atualizar e Excluir) de eventos, trilhas e atividades ao ar livre exclusivo para administradores logados.

## Instruções de Instalação e Execução Local

Siga os passos abaixo para configurar o ambiente de desenvolvimento na sua máquina:

**1. Clone o repositório**
```bash
git clone https://github.com/MateusSantanna/mvp-back-end.git
cd mvp-back-end 
```
**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv

### Ativar no Windows:
venv\Scripts\activate

### Ativar no Linux/Mac:
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Inicie o servidor de desenvolvimento**
```bash

python manage.py runserver
```
A API estará disponível para testes e acesso através de http://127.0.0.1:8000/api/

## Fora do Escopo (O que este MVP não faz):

* Não há um sistema de reservas ou de pagamentos para os eventos, sendo o foco apenas o ecoturismo informativo
* Não existe um sistema de cadastro ou login para usuários comuns/visitantes (apenas para administradores gerenciarem o conteúdo)
* O sistema não envia notificações por e-mail ou SMS de forma automática
