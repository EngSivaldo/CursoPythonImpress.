import tkinter as tk  # Importa a biblioteca tkinter

# Cria a janela principal
janela = tk.Tk()
janela.title('Cotação de Moedas')

# Cria e configura o primeiro rótulo (label)
mensagem = tk.Label(
    text='Sistema de busca de cotação de moedas!',
    bg='black',
    fg='white',
    width=50,
    height=5
)
# Adiciona o rótulo à janela
mensagem.pack()

# Cria e configura o segundo rótulo (label)
mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.pack()

# Cria o campo de entrada (entry) para o usuário digitar a moeda
moeda = tk.Entry()
moeda.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()