import tkinter as tk  # Importa a biblioteca tkinter
from tkinter import ttk  # Importa o módulo ttk para widgets estilizados

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
# moeda = tk.Entry()
# moeda.grid(row=1, column=1)

# Dicionário com as cotações das moedas mais conhecidas em relação ao Real Brasileiro (BRL)
dicionario_cotacoes = {
    'USD': 5.26,  # Dólar Americano
    'EUR': 5.47,  # Euro
    'GBP': 6.63,  # Libra Esterlina
    'JPY': 0.04,  # Iene Japonês
    'CHF': 5.84,  # Franco Suíço
    'CAD': 3.89,  # Dólar Canadense
    'AUD': 3.63,  # Dólar Australiano
    'CNY': 0.79,  # Yuan Chinês
    'INR': 0.06,  # Rúpia Indiana
    'BRL': 1.00  # Real Brasileiro
}

# Lista de moedas para o combobox
moedas = list(dicionario_cotacoes.keys())

# Cria o combobox para selecionar a moeda
moeda = ttk.Combobox(janela, values=moedas)  # Cria um combobox com as moedas disponíveis
moeda.grid(row=1, column=1)  # Posiciona o combobox na linha 1, coluna 1

# Função para buscar a cotação
def buscar_cotacao():
    moeda_preenchida = moeda.get()  # Obtém a moeda selecionada no combobox
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)  # Busca a cotação da moeda no dicionário
    # Cria ou atualiza o rótulo de cotação
    mensagem_cotacao = tk.Label(text='Cotação não encontrada!')  # Cria um rótulo padrão para cotação não encontrada
    mensagem_cotacao.grid(row=3, column=0, columnspan=2)  # Posiciona o rótulo na linha 3, ocupando duas colunas
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'  # Atualiza o texto do rótulo com a cotação encontrada
    else:
        mensagem_cotacao['text'] = 'Cotação não encontrada!'  # Atualiza o texto do rótulo para cotação não encontrada

# Cria o botão para buscar a cotação
botao = tk.Button(text='Buscar Cotação', command=buscar_cotacao)  # Cria um botão que chama a função buscar_cotacao quando clicado
botao.grid(row=2, column=0, columnspan=2)  # Posiciona o botão na linha 2, ocupando duas colunas

# Inicia o loop principal da interface gráfica
janela.mainloop()  # Inicia o loop principal da aplicação, mantendo a janela aberta