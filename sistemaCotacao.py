import tkinter as tk
from tkinter import ttk #combobox
from tkcalendar import DateEntry 

#lista moedas para o combobox
lista_moedas = ['USD', 'EUR']

#para o botao pegar_cotacao
def pegar_cotacao():
  pass

#criar janela ====================================================
janela = tk.Tk()
#titulo da janela
janela.title('Ferramenta de cotação de moedas')

#Labels da moeda unica  ================================
label_cotacao_moeda = tk.Label(text='Cotação de uma moeda específica!', borderwidth=2, relief='solid')
label_cotacao_moeda.grid(row=0, column=0,padx=10, pady=10, sticky='nswe', columnspan=3);

#Labels selecionar moeda==========================================
label_selecionar_moeda = tk.Label(text='Selecionar Moeda!')
label_selecionar_moeda.grid(row=1, column=0,padx=10, pady=10, sticky='nswe', columnspan=2);

#lista suspensa(combobox) que recebe lista_moedas, do label selecionar moeda
combobox_selecionar_moedas = ttk.Combobox(values=[lista_moedas])
combobox_selecionar_moedas.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

#Labels selecionar dia da cotacao =============================
label_selecionar_diaCotacao = tk.Label(text='Selecionar o dia que deseja pegar cotação!')
label_selecionar_diaCotacao.grid(row=2, column=0,padx=10, pady=10, sticky='nswe', columnspan=2);

#calendario do label selecionar dia da cotacao
calendario_moeda = DateEntry(year=2025, locale='pt_BR')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')


#Label texto cotacao cotacao =============================
label_texto_cotacao = tk.Label(text='Pegar cotacao!')
label_texto_cotacao.grid(row=3, column=0,padx=10, pady=10, sticky='nswe', columnspan=2);

botao_pegar_cotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')


#Labels de varias moedas ==================================
label_cotacao_varias_moedas = tk.Label(text='Cotação de Multiplas Moedas!', borderwidth=2, relief='solid')
label_cotacao_varias_moedas.grid(row=4, column=0,padx=10, pady=10, sticky='nswe', columnspan=3);



janela.mainloop()