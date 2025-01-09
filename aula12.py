# Importa a função askopenfilename do módulo tkinter.filedialog
from tkinter.filedialog import askopenfilename
# Importa o módulo pandas e o apelida de pd
import pandas as pd

# Abre uma janela de diálogo para o usuário selecionar um arquivo Excel
caminho_arquivo = askopenfilename(title='Selecione um arquivo em Excel para abrir.')

# Lê o arquivo Excel selecionado e armazena os dados em um DataFrame
df = pd.read_excel(caminho_arquivo)

# Imprime o conteúdo do DataFrame no console
print(df)


# tkinter: Este pacote geralmente já vem instalado com o Python, pois faz parte da biblioteca padrão. No entanto, se você estiver usando uma distribuição do Python que não inclui tkinter, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição (por exemplo, apt-get no Ubuntu).

# pandas: Este pacote precisa ser instalado separadamente. Você pode instalá-lo usando o pip, que é o gerenciador de pacotes do Python. O comando para instalar o pandas é:

# pip install pandas