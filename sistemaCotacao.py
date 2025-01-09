import tkinter as tk
from tkinter import ttk #combobox
from tkcalendar import DateEntry 
import requests


requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()


#lista moedas para o combobox
lista_moedas = list(dicionario_moedas.keys())

#para o botao pegar_cotacao
def pegar_cotacao():
  pass

#botao slecionar_arquivoExcel
def selecionar_arquivoExcel():
  pass

def atualizarCotacao():
  pass


#criar janela ====================================================
janela = tk.Tk()
#titulo da janela
janela.title('Ferramenta de cotação de moedas')

#Labels da moeda unica  ================================
label_cotacao_moeda = tk.Label(text='Cotação de uma moeda específica!', borderwidth=2, relief='solid')
label_cotacao_moeda.grid(row=0, column=0,padx=10, pady=10, sticky='nswe', columnspan=3);

#Labels selecionar moeda==========================================
label_selecionar_moeda = tk.Label(text='Selecionar Moeda!', anchor='e')
label_selecionar_moeda.grid(row=1, column=0,padx=10, pady=10, sticky='nswe', columnspan=2);

# Lista suspensa (combobox) que recebe lista_moedas, do label selecionar moeda
combobox_selecionar_moedas = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moedas.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

#Labels selecionar dia da cotacao =============================
label_selecionar_diaCotacao = tk.Label(text='Selecionar o dia que deseja pegar cotação!', anchor='e')
label_selecionar_diaCotacao.grid(row=2, column=0,padx=10, pady=10, sticky='nswe', columnspan=2);

#calendario do label selecionar dia da cotacao
calendario_moeda = DateEntry(year=2025, locale='pt_BR')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')


#Label texto cotacao cotacao =============================
label_texto_cotacao = tk.Label(text='Pegar cotacao Vazio!', anchor='e')
label_texto_cotacao.grid(row=3, column=0,padx=10, pady=10, sticky='nswe', columnspan=2);

botao_pegar_cotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')


#Labels de cotacao de varias moedas ==================================
label_cotacao_varias_moedas = tk.Label(text='Cotação de Multiplas Moedas!', borderwidth=2, relief='solid')
label_cotacao_varias_moedas.grid(row=4, column=0,padx=10, pady=10, sticky='nswe', columnspan=3);

#Labels de arquivo Excel ==================================
label_selecionar_arquivo = tk.Label(text='Selecione um arquivo Excel com as Moedas na coluna A:')
label_selecionar_arquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe' )

botao_selecionar_arquivoExcel = tk.Button(text='Clique para selecionar Excel', command=selecionar_arquivoExcel)
botao_selecionar_arquivoExcel.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

label_arquivo_selecionado = tk.Label(text='Nenhum arquivo selecinado!', anchor='e')
label_arquivo_selecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='nswe')


label_dataInicial = tk.Label(text='Data Inicial' ,anchor='e')
label_dataInicial.grid(row=7, column=0, padx=10, pady=10, sticky='nswe')

#calendario do label data inicial
calendario_dataInicial = DateEntry(year=2025, locale='pt_BR')
calendario_dataInicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')

label_dataFinal = tk.Label(text='Data Final', anchor='e')
label_dataFinal.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')

#calendario do label data final
calendario_datafinal = DateEntry(year=2025, locale='pt_BR')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

#butao atualizar cotacoes=====================
botao_atualizarCotacoes = tk.Button(text='Atualizar Cotação', command=atualizarCotacao)
botao_atualizarCotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

#label vazio que recebe msg da funcao
labelVazio_atualizarCotacoes = tk.Label(text='label vazio')
labelVazio_atualizarCotacoes.grid(row=9, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

#botao de fechar janela
botao_fecharJanela = tk.Button(text='Fechar', command=janela.quit)
botao_fecharJanela.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()