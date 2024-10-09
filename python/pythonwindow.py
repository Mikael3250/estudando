import tkinter as tk

def on_button_click():
    label.config(text="Vc recebeu um PI QUES DE 500 REAU \n reinicie o programa para mais money")

window = tk.Tk()
window.title("Dinheiro infinito")
window.geometry("800x800")

label = tk.Label(window, text="Quer um pix de 500tão?")
label.pack(pady=20)

button = tk.Button(window, text="R E C E B A !", command=on_button_click)
button.pack(pady=10)

window.mainloop()