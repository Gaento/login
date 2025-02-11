import customtkinter as ctk
import mysql.connector

#Criando conexão com o banco de dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'logins'
)

#Cursor
cursor = conexao.cursor()

#Cor da tela
ctk.set_appearance_mode('dark')

#func
def cadastrar_usuario():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    email = campo_email.get()
    
    if usuario and senha and email:
        try:
            cursor.execute(
                'INSERT INTO cadastrados (nome, senha, email) VALUES (%s, %s, %s)',
                (usuario, senha, email)
            )
            conexao.commit()

            confirmacao_cadastro.configure(text = "Cadastro realizado com sucesso!", fg_color = "green")
            campo_usuario.delete(0, "end")
            campo_senha.delete(0, "end")
            campo_email.delete(0, "end")
        except Exception as e:
            confirmacao_cadastro.configure(text = f"Erro: {e}", fg_color = "red")
    else:
        confirmacao_cadastro.configure(text = "Preencha todos os campos!", fg_color = "red")


#Janela principal
app = ctk.CTk()
app.title('Cadastro no Haen')
app.geometry ('300x400')

#criação dos campos
#Criação do usuario
label_usuario = ctk.CTkLabel(app, text='Usuário', font=("Arial", 16, "bold"))
label_usuario.pack(pady = 10)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite o Usuário desejado', font=("Arial", 12, "bold"), width= 180)
campo_usuario.pack(padx = 10)
#Criação da senha
label_senha = ctk.CTkLabel(app, text='Senha', font=("Arial", 16, "bold"))
label_senha.pack(pady = 10)

campo_senha = ctk.CTkEntry(app, placeholder_text= 'Digite sua senha', font=("Arial", 12, "bold"), width= 180, show = "*")
campo_senha.pack(padx = 10)
#Colocando o gmail/email
label_email = ctk.CTkLabel(app, text='email', font=("Arial", 16, "bold"))
label_email.pack(pady = 10)

campo_email = ctk.CTkEntry(app, placeholder_text= 'coloque seu email', font=("Arial", 12, "bold"), width= 180)
campo_email.pack(padx = 10)

#Botão para confirmar o cadastro
cadastro = ctk.CTkButton(app, 
    text='Cadastrar', 
    command= cadastrar_usuario,
    font=("Arial", 20, "bold"),
    fg_color="#4682B4",
    hover_color="#696969"
    )
cadastro.pack(pady = 20)

#Cofirmando o cadastro
confirmacao_cadastro = ctk.CTkLabel(app, text="", font = ("Arial", 10, "bold"))
confirmacao_cadastro.pack(pady = 5)

#inicialização do app
app.mainloop()