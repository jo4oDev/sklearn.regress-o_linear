import pandas as pd 
import matplotlib.pyplot as plt
from tkinter import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Função para exibir resultado na janela tk. sempre comentem seus codigos;
def exibir_resultado(texto):
    resultado_label.config(text=texto)

# Meu codigo fica dentro desta função para que o botão possa a chamar quando precisar, com o simples toque no
# botão que criamos logo abaixo no script
def estatisticas_gols():
    valores = {
        'lista2': [int(entrada1.get()), int(entrada2.get()), int(entrada3.get()), int(entrada4.get()), int(entrada5.get()), int(entrada6.get()), int(entrada7.get())]
    }

    valores = pd.DataFrame(valores)

    media = valores.lista2.mean()
    mediana = valores.lista2.median()
    moda = valores.lista2.mode()[0]
    desvio_padrao = valores.lista2.std()

    # ajustar um modelo de regressão linear simples
    X = valores.index.values.reshape(-1, 1)
    y = valores['lista2']
    regressor = LinearRegression()
    regressor.fit(X, y)

    # PREVER VALORES
    proximos_jogos = pd.DataFrame({'index': range(len(valores), len(valores) + 5)})
    proximos_jogos['lista2_pred'] = regressor.predict(proximos_jogos['index'].values.reshape(-1, 1))

    texto_estatisticas = f'''
    Média: {media:.2f}
    Mediana: {mediana:.2f}
    Moda: {moda:.2f}
    Desvio Padrão: {desvio_padrao:.2f}
    '''

    previsoes_texto = '\nPrevisões para próximos jogos:\n' + str(proximos_jogos)
    resultado_texto = texto_estatisticas + previsoes_texto

    exibir_resultado(resultado_texto)

# Iniciando a janela Tk com o titulo Previsão vom IA.
janela = Tk()
janela.title("Previsão com IA, matemática e regressão linear:")

titulo = Label(janela, text='Digite os gols marcados nos 7 últimos jogos:', font=("Helvetica", 16, "bold"))
titulo.grid(columnspan=2, padx=20, pady=10)

#CODIGO COMENTADO PARA FUTURAS ATUALIZAÇÕES
#janela.title("Nos ultimos 7 jogos do seu time, quantos gols teve em cada 1 dos 7 jogos")
#titulo2 = Label(janela, text=)

instrucoes = Label(janela, text='Digite os últimos 7 placares de gol, somente do seu time:')
instrucoes.grid(columnspan=2)

# LOGO ABAIXO ESTOU CRIANDO AS LÁCUNAS QUE SERÃO PREENCHIDAS COM OS DADOS DO TIME
# QUE USARAM A COLUNA=0 1 A COLUNA=1  ASSIM ORGANIZANDO AS LINHAS E COLUNAS DA JANELA PUP
entrada1 = Entry(janela, width=5)
entrada1.grid(column=0, row=2, padx=5, pady=5)
entrada2 = Entry(janela, width=5)
entrada2.grid(column=1, row=2, padx=5, pady=5)
entrada3 = Entry(janela, width=5)
entrada3.grid(column=0, row=3, padx=5, pady=5)
entrada4 = Entry(janela, width=5)
entrada4.grid(column=1, row=3, padx=5, pady=5)
entrada5 = Entry(janela, width=5)
entrada5.grid(column=0, row=4, padx=5, pady=5)
entrada6 = Entry(janela, width=5)
entrada6.grid(column=1, row=4, padx=5, pady=5)
entrada7 = Entry(janela, width=5)
entrada7.grid(column=0, row=5, padx=5, pady=5)

#BOTÃO PARA RODAR O CODIGO, E TRAZER A ESTATISTICA PARA O USUARIO, O COMANDO DO BOTÃO E RODAR A FUNÇÃO estatisticas_gols
botao = Button(janela, text='PREVER ESTATÍSTICAS DE GOLS', command=estatisticas_gols)
botao.grid(columnspan=2, padx=20, pady=10)

resultado_label = Label(janela, text='', font=("Helvetica", 12))
resultado_label.grid(columnspan=2, padx=20, pady=10)

# Aqui vemos a função que mantem a janela aberta
janela.mainloop()