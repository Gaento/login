
Sistema de Cadastro de Usuário

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-Completed-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-%E2%9C%94-brightgreen.svg)

## Descrição

Este projeto é um sistema de cadastro de usuários simples, criado com Python utilizando a biblioteca **CustomTkinter** para a interface gráfica e **MySQL** para o armazenamento de dados dos usuários. O programa permite que o usuário crie um novo cadastro fornecendo um nome de usuário, senha e e-mail, e esses dados são armazenados em um banco de dados MySQL.

## Funcionalidades

- Interface gráfica com campos para o nome de usuário, senha e e-mail.
- Validação para garantir que todos os campos sejam preenchidos antes do cadastro.
- Armazenamento seguro de dados no banco de dados MySQL.
- Feedback visual ao usuário informando se o cadastro foi bem-sucedido ou se ocorreu algum erro.

## Requisitos

- **Python 3.x**
- **Bibliotecas**:
  - `customtkinter`: Para criar a interface gráfica.
  - `mysql-connector-python`: Para a conexão com o banco de dados MySQL.

## Como Executar

1. Certifique-se de ter o MySQL instalado e em funcionamento.
2. Crie o banco de dados `logins` e a tabela `cadastrados` no MySQL com a seguinte estrutura:
   ```sql
   CREATE DATABASE logins;
   USE logins;
   CREATE TABLE cadastrados (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(255),
       senha VARCHAR(255),
       email VARCHAR(255)
   );
   ```
3. Instale as dependências com o seguinte comando:
   ```bash
   pip install customtkinter mysql-connector-python
   ```
4. Salve o código em um arquivo Python, por exemplo, `cadastro_usuario.py`.
5. Execute o código:
   ```bash
   python cadastro_usuario.py
   ```
6. Preencha os campos com o nome de usuário, senha e e-mail e clique em "Cadastrar".

## Como Funciona

1. O usuário fornece as informações de **Usuário**, **Senha** e **E-mail** nos campos apropriados.
2. Ao clicar no botão "Cadastrar", o sistema valida os campos. Caso todos os campos estejam preenchidos, os dados são inseridos na tabela `cadastrados` do banco de dados MySQL.
3. Uma mensagem de confirmação é exibida, indicando se o cadastro foi bem-sucedido ou se ocorreu algum erro.
4. Caso algum campo não seja preenchido, uma mensagem de erro será exibida.

## Exemplo de Uso

Após rodar o código, a interface será exibida conforme o exemplo abaixo:

```
+----------------------------+
|       Cadastro no Haen      |
+----------------------------+
| Usuário: [ campo ]          |
| Senha:   [ campo ]          |
| E-mail:  [ campo ]          |
+----------------------------+
| [ Cadastrar ]               |
+----------------------------+

Se o cadastro for bem-sucedido, você verá:
"Cadastro realizado com sucesso!"

Se ocorrer um erro, uma mensagem será exibida:
"Erro: (detalhes do erro)"
```

## Melhorias Futuras

- Adicionar validação de formato de e-mail.
- Implementar funcionalidade de login.
- Implementar a opção de recuperação de senha.
- Melhorar a segurança no armazenamento de senhas (utilizando hashing, por exemplo).

## Autor

Desenvolvido por Gabriel.
