import tkinter as tk

def soma():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text=f"Resultado: {resultado}")

def subtracao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text=f"Resultado: {resultado}")

def multiplicacao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text=f"Resultado: {resultado}")

def divisao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    try:
        resultado = num1 / num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ZeroDivisionError:
        label_resultado.config(text="Erro: divisão por zero.")

app = tk.Tk()
app.title("Calculadora")

label_num1 = tk.Label(app, text="Digite o primeiro número:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(app, text="Digite o segundo número:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(app)
entry_num2.grid(row=1, column=1)

button_soma = tk.Button(app, text="Adição", command=soma)
button_soma.grid(row=2, column=0)

button_subtracao = tk.Button(app, text="Subtração", command=subtracao)
button_subtracao.grid(row=2, column=1)

button_multiplicacao = tk.Button(app, text="Multiplicação", command=multiplicacao)
button_multiplicacao.grid(row=3, column=0)

button_divisao = tk.Button(app, text="Divisão", command=divisao)
button_divisao.grid(row=3, column=1)

label_resultado = tk.Label(app, text="Resultado:")
label_resultado.grid(row=4, columnspan=2)

app.mainloop()