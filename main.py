import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import os
import random
import winsound
from PIL import ImageTk, Image 

def otworz_github():
    webbrowser.open("https://github.com/1ex7ir")

def fake_bluescreen():
    winsound.MessageBeep(winsound.MB_ICONHAND)
    bsod = tk.Toplevel()
    bsod.attributes("-fullscreen", True)
    bsod.configure(bg="#0078d7") 

    tk.Label(
        bsod,
        text=":(",
        font=("Segoe UI", 80),
        fg="white",
        bg="#0078d7"
    ).pack(anchor="w", padx=100, pady=(100, 10))

    
    tekst = (
        "Komputer napotkał problem i należy go uruchomić ponownie.\n"
        "Trwa zbieranie informacji o błędzie. Po zakończeniu tego procesu\n"
        "komputer zostanie automatycznie uruchomiony ponownie.\n\n"
        "Ukończono 0%\n"
    )
    tk.Label(
        bsod,
        text=tekst,
        font=("Segoe UI", 16),
        fg="white",
        bg="#0078d7",
        justify="left"
    ).pack(anchor="w", padx=100)

    qr_path = os.path.join(os.path.dirname(__file__), "fakeqr.png")  
    if os.path.exists(qr_path):
        qr_img = Image.open(qr_path)
        qr_img = qr_img.resize((120, 120), Image.ANTIALIAS)
        qr = ImageTk.PhotoImage(qr_img)
        tk.Label(bsod, image=qr, bg="#0078d7").pack(anchor="w", padx=100, pady=(10, 5))
        bsod.qr = qr  

    info = (
        "Aby uzyskać więcej informacji o tym problemie i możliwych rozwiązaniach, odwiedź\n"
        "stronę https://www.windows.com/stopcode\n\n"
        "Kod zatrzymania: CRITICAL_PROCESS_DIED"
    )
    tk.Label(
        bsod,
        text=info,
        font=("Segoe UI", 10),
        fg="white",
        bg="#0078d7",
        justify="left"
    ).pack(anchor="w", padx=100)

    bsod.after(6000, bsod.destroy, messagebox.askquestion(
        "Prank!",
        ";)",
        icon='info'
    ))


def uruchom_fake_bs():
    okno = tk.Toplevel()
    okno.title("Ścinaware re1")
    okno.geometry("300x100")
    okno.resizable(False, False)
    folder = os.path.dirname(os.path.abspath(__file__))
    ikona = os.path.join(folder, "icon.ico")

    if os.path.exists(ikona):
        okno.iconbitmap(ikona)

    etykieta = tk.Label(okno, text="Ścinaware pracuje!", font=("Arial", 12))
    etykieta.pack(pady=10)

    pasek = ttk.Progressbar(okno, orient="horizontal", length=250, mode="determinate", maximum=100)
    pasek.pack(pady=5)

    def ladowanie(i=0):
        if i > 100:
            i = 0
        pasek['value'] = i
        okno.after(45, lambda: ladowanie(i + 1))

    ladowanie()

    okno.after(4500, fake_bluescreen)


def ostrzezenie_bs():
    decyzja = messagebox.askquestion(
        "Uwaga!",
        "FAKE BLUE SCREEN SPOWODUJE PEŁNOEKRANOWE ZAMROŻENIE SYSTEMU NA KILKA SEKUND.\n\nCZY NA PEWNO CHCESZ KONTYNUOWAĆ?",
        icon='warning'
    )
    if decyzja == 'yes':
        uruchom_fake_bs()


def uruchom_skrypty():
    okno = tk.Toplevel()
    okno.title("Ścinaware re1")
    okno.geometry("300x100")
    okno.resizable(False, False)
    folder = os.path.dirname(os.path.abspath(__file__))
    ikona = os.path.join(folder, "icon.ico")

    if os.path.exists(ikona):
        okno.iconbitmap(ikona)

    etykieta = tk.Label(okno, text="Ścinaware pracuje!", font=("Arial", 12))
    etykieta.pack(pady=10)

    pasek = ttk.Progressbar(okno, orient="horizontal", length=250, mode="determinate", maximum=100)
    pasek.pack(pady=5)

    def ladowanie(i=0):
        if i > 100:
            i = 0
        pasek['value'] = i
        okno.after(45, lambda: ladowanie(i + 1))

    ladowanie()

    hta = os.path.join(folder, "cos.hta")
    vbs = os.path.join(folder, "cos.vbs")

    def odpal_skrypty():
        if os.path.exists(hta):
            os.startfile(hta)
        else:
            print("Nie znaleziono pliku:", hta)
        if os.path.exists(vbs):
            os.startfile(vbs)
        else:
            print("Nie znaleziono pliku:", vbs)

    okno.after(4500, odpal_skrypty)


def uruchom_skrypty2():
    okno = tk.Toplevel()
    okno.title("Ścinaware re1")
    okno.geometry("300x100")
    okno.resizable(False, False)
    folder = os.path.dirname(os.path.abspath(__file__))
    ikona = os.path.join(folder, "icon.ico")

    if os.path.exists(ikona):
        okno.iconbitmap(ikona)

    etykieta = tk.Label(okno, text="Ścinaware pracuje!", font=("Arial", 12))
    etykieta.pack(pady=10)

    pasek = ttk.Progressbar(okno, orient="horizontal", length=250, mode="determinate", maximum=99)
    pasek.pack(pady=5)

    def ladowanie(i=0):
        if i > 100:
            i = 0
        pasek['value'] = i
        okno.after(45, lambda: ladowanie(i + 1))

    ladowanie()

    okno.after(4500, lambda: messagebox.showinfo("Work in progress.", "Test skończony!"))


def ostrzezenie1():
    decyzja = messagebox.askquestion(
        "Uwaga!",
        "OPCJA TA UNIEMOŻLIWI KORZYSTANIE Z TEGO URZĄDZENIA I WYMAGANY BĘDZIE RESTART.\n\nCZY NA PEWNO CHCESZ KONTYNUOWAĆ?",
        icon='warning'
    )
    if decyzja == 'yes':
        uruchom_skrypty()


def ostrzezenie2():
    decyzja2 = messagebox.showinfo(
        "Work in progress!",
        'Opcja ta służy wyłącznie do testów UI, zapraszamy do skorzystania z opcji obok, aby rozpocząć proces lagowania :)!',
        icon='info'
    )
    if decyzja2 == 'ok':
        uruchom_skrypty2()


okno = tk.Tk()
okno.title("Ścinaware re1")
okno.geometry("450x220")
okno.resizable(False, False)
folder = os.path.dirname(os.path.abspath(__file__))
ikona = os.path.join(folder, "icon.ico")

if os.path.exists(ikona):
    okno.iconbitmap(ikona)

ramka = tk.Frame(okno)
ramka.pack(pady=10)

tk.Label(ramka, text="Witaj w", font=("Comic Sans MS", 17)).pack(side="left")
tk.Label(ramka, text="Ścinaware", font=("Comic Sans MS", 17, "italic", "underline"), fg="red").pack(side="left")

ramka_przyciski = tk.Frame(okno)
ramka_przyciski.pack(pady=10)

tk.Button(ramka_przyciski, text="Ścinaj", command=ostrzezenie1, font=("Comic Sans MS", 11)).pack(side="left", padx=5)
tk.Button(ramka_przyciski, text="UI TEST", command=ostrzezenie2, font=("Comic Sans MS", 11)).pack(side="left", padx=5)
tk.Button(ramka_przyciski, text="Fake BS", command=ostrzezenie_bs, font=("Comic Sans MS", 11), fg="blue").pack(side="left", padx=5)

ramka_dol = tk.Frame(okno)
ramka_dol.pack(pady=5)

tk.Label(ramka_dol, text="Wbij na:", font=("Comic Sans MS", 8)).pack(side="left", padx=5)
tk.Button(ramka_dol, text="GitHub", command=otworz_github, fg="red", font=("Comic Sans MS", 8)).pack(side="left")

ramka_opis = tk.Frame(okno)
ramka_opis.pack(side="bottom", pady=5)

tk.Label(ramka_opis, text="Ścinaware to aplikacja, do zabawy twoim urządzeniem", font=("Comic Sans MS", 8)).pack()

wersja = tk.Frame(okno)
wersja.pack(side="bottom", pady=5)

tk.Label(wersja, text="Version: re1", font=("Arial", 7)).pack()

okno.mainloop()
