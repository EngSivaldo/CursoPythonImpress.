import tkinter as tk
from tkinter import ttk

# Cria a janela principal
janela = tk.Tk()
janela.title('Cotação de Moedas')

# Configura a janela para ajustar o tamanho das linhas e colunas
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

# Cria e configura o primeiro rótulo (label)
mensagem = tk.Label(
    text='Sistema de busca de cotação de moedas!',
    bg='black',
    fg='white',
    width=35,
    height=5
)
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')

# Cria e configura o segundo rótulo (label)
mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.grid(row=1, column=0)

# Dicionário com as cotações das moedas mais conhecidas
dicionario_cotacoes = {
    'USD': 5.26,
    'EUR': 5.47,
    'GBP': 6.63,
    'JPY': 0.04,
    'CHF': 5.84,
    'CAD': 3.89,
    'AUD': 3.63,
    'CNY': 0.79,
    'INR': 0.06,
    'BRL': 1.00
}

# Lista de moedas para o combobox
moedas = list(dicionario_cotacoes.keys())

# Cria o combobox para selecionar a moeda
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

# Função para buscar a cotação
def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text='Cotação não encontrada!')
    mensagem_cotacao.grid(row=3, column=0, columnspan=2)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'
    else:
        mensagem_cotacao['text'] = 'Cotação não encontrada!'

# Cria o botão para buscar a cotação
botao = tk.Button(text='Buscar Cotação', command=buscar_cotacao)
botao.grid(row=2, column=0, columnspan=2)

# Mensagem para múltiplas cotações
mensagem3 = tk.Label(text='Caso queira pegar cotação de mais de uma moeda ao mesmo tempo, digite uma em cada linha!')
mensagem3.grid(row=4, column=0, columnspan=2)

# Caixa de texto para múltiplas cotações
caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky='nswe')

# Função para buscar múltiplas cotações
def buscar_cotacoes():
    texto = caixa_texto.get('1.0', tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacacao = dicionario_cotacoes.get(item)
        if cotacacao:
            mensagem_cotacoes.append(f'{item}: {cotacacao}')
    mensagem4 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=1)

# Botão para buscar múltiplas cotações
botao_multiplasCotacoes = tk.Button(text='Buscar Cotações', command=buscar_cotacoes)
botao_multiplasCotacoes.grid(row=5, column=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()
