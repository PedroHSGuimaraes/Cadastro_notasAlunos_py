from tkinter import *


def cadastrar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()
    nota = entry_nota.get()
    label_cadastro["text"] = "Aluno cadastrado:\nNome: {}\nIdade: {}\nNota: {}".format(nome, idade, nota)


janela = Tk(
    screenName="Cadastro de Alunos",
)
janela.title("Cadastro de Alunos")
janela.geometry("300x300")
janela.resizable(False, False)


label_nome = Label(janela, text="Nome:")
label_nome.pack(pady=10)

entry_nome = Entry(janela, width=20)
entry_nome.pack()

label_idade = Label(janela, text="Idade:")
label_idade.pack(pady=10)

entry_idade = Entry(janela, width=20)
entry_idade.pack()

label_nota = Label(janela, text="Nota:")
label_nota.pack(pady=10)

entry_nota = Entry(janela, width=20)
entry_nota.pack()

btn_cadastrar = Button(janela, text="Cadastrar", command=cadastrar_aluno)
btn_cadastrar.pack(pady=10)

label_cadastro = Label(janela, text="")
label_cadastro.pack(pady=10)

janela.mainloop()