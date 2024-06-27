import tkinter as tk

janela = tk.Tk()
janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a Moeda desejada: ")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)



def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text="Cotação Não Encontrada")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"Cotação do{moeda_preenchida} é de {cotacao_moeda} reais."
    print(moeda.get())

dicionario_cotacoes = {
    "Dolar" : "5.50",
    "Euro" : "6.50",
    "Libra": "7.50",
    "Yen": "0.50",
    "Won": "0.50"}

botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()
