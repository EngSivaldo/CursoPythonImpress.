import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import requests
import pandas as pd
from tkinter.filedialog import askopenfilename

# Função para obter a cotação de uma moeda específica
def pegar_cotacao():
    moeda = combobox_selecionar_moedas.get()
    data = calendario_moeda.get_date().strftime('%Y-%m-%d')
    url = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={data}&end_date={data}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados:
            cotacao = dados[0]['bid']
            label_texto_cotacao.config(text=f"Cotação do {moeda} em {data}: {cotacao}")
        else:
            label_texto_cotacao.config(text="Cotação não encontrada para a data selecionada.")
    else:
        label_texto_cotacao.config(text="Erro ao obter cotação. Verifique o código da moeda.")

# Função para selecionar arquivo Excel
def selecionar_arquivoExcel():
    caminho_arquivo = askopenfilename(title='Selecione um arquivo em Excel para abrir.')
    if caminho_arquivo:
        df = pd.read_excel(caminho_arquivo)
        label_arquivo_selecionado.config(text=f"Arquivo selecionado: {caminho_arquivo}")
        # Aqui você pode adicionar a lógica para processar o arquivo Excel
    else:
        label_arquivo_selecionado.config(text="Nenhum arquivo selecionado!")

# Função para atualizar cotações
def atualizarCotacao():
    data_inicial = calendario_dataInicial.get_date().strftime('%Y-%m-%d')
    data_final = calendario_datafinal.get_date().strftime('%Y-%m-%d')
    # Aqui você pode adicionar a lógica para atualizar as cotações entre as datas selecionadas
    labelVazio_atualizarCotacoes.config(text=f"Cotações atualizadas de {data_inicial} a {data_final}")

# Requisição para obter lista de moedas
requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()
lista_moedas = list(dicionario_moedas.keys())

# Criar janela
janela = tk.Tk()
# Título da janela
janela.title('Ferramenta de cotação de moedas')

# Labels da moeda única
label_cotacao_moeda = tk.Label(text='Cotação de uma moeda específica!', borderwidth=2, relief='solid')
label_cotacao_moeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

# Labels selecionar moeda
label_selecionar_moeda = tk.Label(text='Selecionar Moeda!', anchor='e')
label_selecionar_moeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

# Lista suspensa (combobox) que recebe lista_moedas, do label selecionar moeda
combobox_selecionar_moedas = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moedas.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

# Labels selecionar dia da cotação
label_selecionar_diaCotacao = tk.Label(text='Selecionar o dia que deseja pegar cotação!', anchor='e')
label_selecionar_diaCotacao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

# Calendário do label selecionar dia da cotação
calendario_moeda = DateEntry(year=2025, locale='pt_BR')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

# Label texto cotação
label_texto_cotacao = tk.Label(text='Pegar cotação Vazio!', anchor='e')
label_texto_cotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_pegar_cotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Labels de cotação de várias moedas
label_cotacao_varias_moedas = tk.Label(text='Cotação de Múltiplas Moedas!', borderwidth=2, relief='solid')
label_cotacao_varias_moedas.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

# Labels de arquivo Excel
label_selecionar_arquivo = tk.Label(text='Selecione um arquivo Excel com as Moedas na coluna A:')
label_selecionar_arquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_selecionar_arquivoExcel = tk.Button(text='Clique para selecionar Excel', command=selecionar_arquivoExcel)
botao_selecionar_arquivoExcel.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

label_arquivo_selecionado = tk.Label(text='Nenhum arquivo selecionado!', anchor='e')
label_arquivo_selecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='nswe')

label_dataInicial = tk.Label(text='Data Inicial', anchor='e')
label_dataInicial.grid(row=7, column=0, padx=10, pady=10, sticky='nswe')

# Calendário do label data inicial
calendario_dataInicial = DateEntry(year=2025, locale='pt_BR')
calendario_dataInicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')

label_dataFinal = tk.Label(text='Data Final', anchor='e')
label_dataFinal.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')

# Calendário do label data final
calendario_datafinal = DateEntry(year=2025, locale='pt_BR')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

# Botão atualizar cotações
botao_atualizarCotacoes = tk.Button(text='Atualizar Cotação', command=atualizarCotacao)
botao_atualizarCotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

# Label vazio que recebe mensagem da função
labelVazio_atualizarCotacoes = tk.Label(text='Label vazio')
labelVazio_atualizarCotacoes.grid(row=9, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

# Botão de fechar janela
botao_fecharJanela = tk.Button(text='Fechar', command=janela.quit)
botao_fecharJanela.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()