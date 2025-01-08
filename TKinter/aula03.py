import tkinter as tk  #bibliotecca inteira


janela = tk.Tk()  #cria a janela
janela.title('Cotação de moedas!')

#cria  o objeto
mensagem = tk.Label(text='Sistema de busca de cotação de moedas!', bg='black' ,fg='white', width='100', height='50')
#inseri objeto dentro da janela
mensagem.pack()

mensagem2 =tk.Label(text='Selecione a moeda desejada nnnnnnnnnnnnnnnnnnnnnn', bg='red' ,fg='white',  width='100', height='100')
mensagem2.pack()

janela.mainloop()