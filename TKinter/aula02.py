import tkinter as tk  #bibliotecca inteira


janela = tk.Tk()  #cria a janela
janela.title('Cotação de moedas!')

#cria  o objeto
mensagem = tk.Label(text='Sistema de busca de cotação de moedas!')
#inseri objeto dentro da janela
mensagem.pack()

mensagem2 =tk.Label(text='Selecione a moeda desejada')
mensagem2.pack()

janela.mainloop()