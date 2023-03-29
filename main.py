import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# Create the main window
okno = tk.Tk()
okno.title("Konfigurátor HAMBURGERU")
okno.geometry("300x550")
okno.resizable(width=True, height=True)
okno.minsize(width=300, height=550)

# Create the hamburger customization options
nazev_burgeru = tk.StringVar()
zemle = tk.StringVar()
maso = tk.StringVar()
zelenina = tk.StringVar()
omacka = tk.StringVar()

# Create the widgets for the hamburger customization options
# NAZEV BURGERU
nazev_burgeru_label = tk.Label(okno, text="Zadejte jméno pro váš burger:")
nazev_burgeru_label.pack()
nazev_burgeru_textinput = tk.Entry(okno, textvariable=nazev_burgeru)
nazev_burgeru_textinput.pack()

# ZEMLE
zemle_label = tk.Label(okno, text="Vyberte si žemli:")
zemle_label.pack()

# Make the default value of the zemle variable "sezam"
zemle.set("sezam")
zemle_radio1 = tk.Radiobutton(okno, text="sezam", variable=zemle, value="sezam")
zemle_radio1.pack()

zemle_radio2 = tk.Radiobutton(okno, text="tmava", variable=zemle, value="tmava")
zemle_radio2.pack()

zemle_radio3 = tk.Radiobutton(okno, text="svetla", variable=zemle, value="svetla")
zemle_radio3.pack()

# MASO
maso_label = tk.Label(okno, text="Zvolte si druh masa:")
maso_label.pack()

# Make the default value of the maso variable "kureci"
maso.set("kureci")
maso_radio2 = tk.Radiobutton(okno, text="kureci", variable=maso, value="kureci")
maso_radio2.pack()

maso_radio1 = tk.Radiobutton(okno, text="hovezi", variable=maso, value="hovezi")
maso_radio1.pack()


# ZELENINA
zelenina_label = tk.Label(okno, text="Vyberte zeleninu:")
zelenina_label.pack()

zelenina1 = tk.IntVar()
zelenina_radio1 = tk.Checkbutton(okno, text="salat", variable=zelenina1)
zelenina_radio1.pack()

zelenina2 = tk.IntVar()
zelenina_radio2 = tk.Checkbutton(okno, text="rajce", variable=zelenina2)
zelenina_radio2.pack()

zelenina3 = tk.IntVar()
zelenina_radio3 = tk.Checkbutton(okno, text="cibule", variable=zelenina3)
zelenina_radio3.pack()

zelenina4 = tk.IntVar()
zelenina_radio4 = tk.Checkbutton(okno, text="okurky", variable=zelenina4)
zelenina_radio4.pack()

# OMACKA
omacka_label = tk.Label(okno, text="Zvolte omáčku:")
omacka_label.pack()

omacka1 = tk.IntVar()
omacka_radio1 = tk.Checkbutton(okno, text="sweetchilli", variable=omacka1)
omacka_radio1.pack()

omacka2 = tk.IntVar()
omacka_radio2 = tk.Checkbutton(okno, text="sladkokysela", variable=omacka2)
omacka_radio2.pack()

omacka3 = tk.IntVar()
omacka_radio3 = tk.Checkbutton(okno, text="kecup", variable=omacka3)
omacka_radio3.pack()

omacka4 = tk.IntVar()
omacka_radio4 = tk.Checkbutton(okno, text="barbecue", variable=omacka4)
omacka_radio4.pack()
# Create the submit button
def submit():
    # Create a list to store the selected vegetables
    zelenina_value = []
    if zelenina1.get():
        zelenina_value.append("salat")
    if zelenina2.get():
        zelenina_value.append("rajce")
    if zelenina3.get():
        zelenina_value.append("cibule")
    if zelenina4.get():
        zelenina_value.append("okurky")

    # Create a list to store the selected sauces
    omacka_value = []
    if omacka1.get():
        omacka_value.append("sweetchilli")
    if omacka2.get():
        omacka_value.append("sladkokysela")
    if omacka3.get():
        omacka_value.append("kecup")
    if omacka4.get():
        omacka_value.append("barbecue")

    # Clear the window
    for widgets in okno.winfo_children():
        widgets.destroy()

    # Create the image
    komponenty = []
    top_bun = f"{zemle.get()}-top"
    komponenty.append(top_bun)

    for zelenina in zelenina_value:
        komponenty.append(zelenina)

    for omacka in omacka_value:
        komponenty.append(omacka)

    komponenty.append(maso.get())

    bottom_bun = f"{zemle.get()}-bottom"
    komponenty.append(bottom_bun)

    burger_pozadi = Image.new("RGBA", (500, 900), (255, 255, 255, 0))

    # print(komponenty)
    # print(zelenina_value)
    # print(omacka_value)
    osa_y = 25
    for komponent in komponenty:
        cesta_k_obrazku = f"./img/{komponent}.png"
        komponent_img = Image.open(cesta_k_obrazku)
        burger_pozadi.paste(komponent_img, (150, osa_y), komponent_img)
        osa_y += 110

    # Create the final image
    final_image = ImageTk.PhotoImage(burger_pozadi)
    final_image_label = tk.Label(okno, image=final_image)
    final_image_label.image = final_image
    final_image_label.pack()

    okno.minsize(width=300, height=1200)


# Show the submit button
submit_button = tk.Button(okno, text="Potvrdit", command=submit)
submit_button.pack()

# Run the mainloop
okno.mainloop()

