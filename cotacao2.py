import tkinter as tk
import yfinance as yf
from tkinter import ttk

janela = tk.Tk()
janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a Moeda desejada: ")
mensagem2.grid(row=1, column=0)

# Lista de moedas
moedas = ["USD", "CAD", "GBP"]
moeda_selecionada = tk.StringVar()
moeda_combobox = ttk.Combobox(janela, textvariable=moeda_selecionada, values=moedas)
moeda_combobox.grid(row=1, column=1)
moeda_combobox.set("Selecione uma moeda")

def buscar_cotacao():
    moeda_preenchida = moeda_selecionada.get()
    symbol = f"{moeda_preenchida}BRL=X"

    try:
        cotacao = yf.Ticker(symbol).history(period="1d")['Close'][0]
        mensagem_cotacao = tk.Label(text=f"Cotação do {moeda_preenchida} é de {cotacao:.2f} BRL.")
        mensagem_cotacao.grid(row=3, column=0, columnspan=2)
    except Exception as e:
        mensagem_cotacao = tk.Label(text="Cotação Não Encontrada ou Erro ao buscar cotação")
        mensagem_cotacao.grid(row=3, column=0, columnspan=2)
        print(f"Erro: {e}")

botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()
