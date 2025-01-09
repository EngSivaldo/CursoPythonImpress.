import tkinter as tk;

janela = tk.Tk();

var_promocoes = tk.IntVar();
checkbox_promocoes = tk.Checkbutton(text='Deseja receber e-mail promocional?', variable=var_promocoes, width=30, height=5);
checkbox_promocoes.grid(row=0, column=0);

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text='Aceitar termos de Uso e Politica de privacidade', variable=var_politicas)
checkbox_politicas.grid(row=1, column=0)

def enviar():
  print(var_promocoes.get())
  if var_promocoes.get() == 1:
    print('usuário deseja receber promoções')  
  else:
    print('usuário Não deseja receber promoções!')
  if var_politicas.get():
    print('Usuário concordou com termos de Uso e politica de Privacidade.')
  else:
     print('Usuário Não concordou com termos de Uso e politica de Privacidade.')



botao_enviar = tk.Button(text='Enviar', command=enviar);
botao_enviar.grid(row=2, column=0)


janela.mainloop();