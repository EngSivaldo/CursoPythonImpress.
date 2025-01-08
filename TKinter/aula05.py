import tkinter as tk  # Importa a biblioteca tkinter

# Cria a janela principal
janela = tk.Tk()  # Inicializa a janela principal da aplicação
janela.title('Cotação de Moedas')  # Define o título da janela

# Configura a janela para ajustar o tamanho das linhas e colunas
janela.rowconfigure(0, weight=1)  # Configura a linha 0 para expandir conforme necessário
janela.columnconfigure([0, 1], weight=1)  # Configura as colunas 0 e 1 para expandir conforme necessário

# Cria e configura o primeiro rótulo (label)
mensagem = tk.Label(
    text='Sistema de busca de cotação de moedas!',  # Define o texto do rótulo
    bg='black',  # Define a cor de fundo do rótulo como preto
    fg='white',  # Define a cor do texto do rótulo como branco
    width=35,  # Define a largura do rótulo
    height=5  # Define a altura do rótulo
)
# Adiciona o rótulo à janela
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')  # Posiciona o rótulo na grade, ocupando duas colunas e expandindo em todas as direções

# Cria e configura o segundo rótulo (label)
mensagem2 = tk.Label(text='Selecione a moeda desejada')  # Cria um rótulo com o texto especificado
mensagem2.grid(row=1, column=0)  # Posiciona o rótulo na linha 1, coluna 0

# Cria o campo de entrada (entry) para o usuário digitar a moeda
moeda = tk.Entry()  # Cria um campo de entrada de texto
moeda.grid(row=1, column=1)  # Posiciona o campo de entrada na linha 1, coluna 1

# Inicia o loop principal da interface gráfica
janela.mainloop()  # Inicia o loop principal da aplicação, mantendo a janela aberta