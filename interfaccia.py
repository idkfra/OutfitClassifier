from tkinter import *

from tkinter import messagebox 
import tkinter as tk
from tkinter import ttk




window = tk.Tk()
window.title('Prova fia')
window.geometry("600x600")


#controllo su click di più colori
def mostra_selezione():
    selezioni = [colore for colore, valore in colori.items() if valore.get() == 1]
    if len(selezioni) > 2:
        messagebox.showerror("Errore", "Puoi selezionare al massimo due colori.")
    else:
        messagebox.showinfo("Selezione colori", f"I colori selezionati sono: {', '.join(selezioni)}")


#scelta stagione
label_stagione = Label(window, text="Stagione:", font=("Helvetica", 12, "bold"))
label_stagione.pack(padx=5, pady=5)

stagioni = ['Inverno', 'Primavera', 'Estate', 'Autunno']
stagione = StringVar(window)
stagione.set(stagioni[0])

menu_stagione = OptionMenu(window, stagione, *stagioni)
menu_stagione.pack(padx=5, pady=5)


#scelta colori
label_scegli_colore = Label(window, text="Scegli i colori:", font=("Helvetica", 10, "bold"))
label_scegli_colore.pack(padx=5, pady=5)

colori_frame = Frame(window)  # Frame per organizzare i colori
colori_frame.pack(padx=5, pady=5)

colori = {
    'Beige': IntVar(),
    'Blu': IntVar(),
    'Verde': IntVar(),
    'Giallo': IntVar(),
    'Nero': IntVar(),
    'Azzurro': IntVar(),
    'Arancione': IntVar(),
    'Rosa': IntVar(),
    'Rosso': IntVar(),
    'Viola': IntVar(),
    'Grigio': IntVar(),
    'Bianco': IntVar(),
    'Lilla': IntVar()
}

row_counter = 0
column_counter = 0

for colore, valore in colori.items():
    Checkbutton(colori_frame, text=colore, variable=valore, font=("Helvetica", 10)).grid(row=row_counter, column=column_counter, padx=5, pady=5)
    row_counter += 1
    if row_counter == len(colori) // 3:  # Passa alla seconda colonna dopo aver disposto metà dei colori
        row_counter = 0
        column_counter += 1



#scelta sesso
sesso = tk.IntVar()

tk.Label(window, 
        text="""Sesso:""", 
        font = ("HELVETICA", 10, "bold"),
        justify = tk.CENTER,
        padx = 20).pack()

frame = tk.Frame(window)
frame.pack()
tk.Radiobutton(frame, 
               text="Femmina",
               padx = 20, 
               variable=sesso, 
               value=0).pack(side=tk.LEFT, padx=5, pady=5)

tk.Radiobutton(frame, 
               text="Maschio",
               padx = 20, 
               variable=sesso, 
               value=1).pack( side=tk.LEFT, padx=5, pady=5)


#scelta occasione


label_occasione = tk.Label(window, text="Per quale occasione utilizzerai questo outfit?" , font=("Helvetica", 10, "bold"))
label_occasione.pack(padx=5, pady=5)

comboExample = ttk.Combobox(window, values=["Svago", "Occasione formale", "Scuola", "Lavoro"])
print(dict(comboExample))
comboExample.pack(padx=5, pady=5)
comboExample.current(1)

print(comboExample.current(), comboExample.get())   


#scelta stile abbigliamento

label_stile_abbigliamento = tk.Label(window, text="Che stile ha il tuo outfit?", font=("Helvetica", 10, "bold"))
label_stile_abbigliamento.pack(padx=5, pady=5)

comboExample = ttk.Combobox(window, values=["Elegante", "Streetwear", "Casual", "Sportivo"])
print(dict(comboExample))
comboExample.pack(padx=5, pady=5)
comboExample.current(1)

print(comboExample.current(), comboExample.get())   





#scelta top

topvar = tk.IntVar()
topvar.set(0)  # initializing the choice, i.e. Python



tk.Label(window, text="""Quale indumento top indossi?""", 
         font=("HELVETICA", 10, "bold"),
         justify=tk.CENTER).pack(padx=5, pady=5)

frame = tk.Frame(window)
frame.pack()

R1 = Radiobutton(frame, text="camicia", variable=topvar, value=0)
R1.pack(side=tk.LEFT, padx=5, pady=5)
R2 = Radiobutton(frame, text="felpa", variable=topvar, value=1)
R2.pack(side=tk.LEFT, padx=5, pady=5)
R3 = Radiobutton(frame, text="giacca", variable=topvar, value=2)
R3.pack(side=tk.LEFT, padx=5, pady=5)
R3 = Radiobutton(frame, text="maglia", variable=topvar, value=3)
R3.pack(side=tk.LEFT, padx=5, pady=5)





#scelta bottom

topvar = tk.IntVar()
topvar.set(1)  # initializing the choice, i.e. Python

tk.Label(window, text="""Quale indumento bottom indossi?""", 
         font=("HELVETICA", 10, "bold"),
         justify=tk.CENTER).pack(padx=5, pady=5)

frame = tk.Frame(window)
frame.pack()

R1 = Radiobutton(frame, text="gonna", variable=topvar, value=0)
R1.pack(side=tk.LEFT, padx=5, pady=5)
R2 = Radiobutton(frame, text="pantalone", variable=topvar, value=1)
R2.pack(side=tk.LEFT, padx=5, pady=5)
R3 = Radiobutton(frame, text="pantalone corto", variable=topvar, value=2)
R3.pack(side=tk.LEFT, padx=5, pady=5)



btn_mostra = Button(window, text="Mostra selezione", command=mostra_selezione, font=("Helvetica", 12))
btn_mostra.pack(padx=5, pady=5)


window.mainloop()