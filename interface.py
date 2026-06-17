import customtkinter as ctk
from tkinter import messagebox

from turing_machine import is_prime_turing

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def verificar():
    try:
        numero_decimal = int(entrada.get())

        numero_binario = bin(numero_decimal)[2:]

        resultado = is_prime_turing(numero_binario)

        texto = (
            f"Decimal: {numero_decimal}\n"
            f"Binário: {numero_binario}\n\n"
            f"{'Número Primo ✅' if resultado else 'Número Não Primo ❌'}"
        )

        resultado_label.configure(text=texto)

    except:
        messagebox.showerror(
            "Erro",
            "Digite um número válido"
        )


app = ctk.CTk()
app.title("Máquina de Turing")
app.geometry("600x400")

titulo = ctk.CTkLabel(
    app,
    text="Validador de Números Primos",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=20)

entrada = ctk.CTkEntry(
    app,
    placeholder_text="Digite um número decimal",
    width=300,
    height=40
)
entrada.pack(pady=30)

botao = ctk.CTkButton(
    app,
    text="Verificar",
    command=verificar,
    width=200,
    height=40
)
botao.pack()

resultado_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 16)
)
resultado_label.pack(pady=30)

app.mainloop()