import tkinter as tk  # Importa a biblioteca tkinter

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
# Adiciona o rótulo à janela
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')

# Cria e configura o segundo rótulo (label)
mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.grid(row=1, column=0)

# Cria o campo de entrada (entry) para o usuário digitar a moeda
moeda = tk.Entry()
moeda.grid(row=1, column=1)

cotacoes_para_brl = {
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

def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = cotacoes_para_brl.get(moeda_preenchida)
    #criar label
    mensagem_cotacao = tk.Label(text='Cotação não encontrada!')
    mensagem_cotacao.grid(row=3, column=0)
    if(cotacao_moeda):
        mensagem_cotacao['text'] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'
    else:
        mensagem_cotacao['text']



botao = tk.Button(text='buscar cotação', command=buscar_cotacao)
botao.grid(row=3, column=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()