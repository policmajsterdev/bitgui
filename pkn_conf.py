import os
import requests
from bs4 import BeautifulSoup
import pickle
from tkinter import *
from tkinter import messagebox as msb
from passlib.hash import pbkdf2_sha256
import data_gen


filepath = os.path.dirname(__file__)


def window_pkn_game(adres_tablicy, punkty):

    wstep = "Wysyłasz [ " + punkty + " ] punktów do tablicy wyników!"
    root = Tk()
    root.geometry("500x200")
    root.title(wstep)

    # Buttony

    text1_lbl = Label(root, text="Za chwilę wyślesz wiadomość do blockchain BSV! ♡", fg="#006666")
    text1_lbl.place(x=120, y=10)

    text_lbl = Label(root, text="Wpisz swój nick : ")
    text_lbl.place(x=80, y=50)

    tresc_entry = Entry(root, width=30)
    tresc_entry.place(x=220, y=50)

    but_dalej = Button(root, text="Dalej", bg="#009900", command=lambda: dalej_2_game(tresc_entry.get(), root, adres_tablicy, punkty))
    but_dalej.place(x=410, y=46)

    text2_lbl = Label(root, text="Zero ukrytych opłat! :)", fg="#008080")
    text2_lbl.place(x=10, y=130)
    text3_lbl = Label(root, text="☆  0.0002 BSV przesyłasz na tablicę wyników.", fg="#008080")
    text3_lbl.place(x=20, y=150)
    text4_lbl = Label(root, text="☆  0.00000250 BSV przesyłasz górnikowi by potwierdzić transkację.", fg="#008080")
    text4_lbl.place(x=20, y=170)
    root.mainloop()


def dalej_2_game(nazwa_gracza, window, adres_tab, points):

    if not nazwa_gracza:
        msb.showwarning(title="Błąd", message="Nie możesz wysłać pustej wiadomości.")
    else:
        print(nazwa_gracza, adres_tab, points)
        text1_lbl = Label(window, text=nazwa_gracza, fg="#006666")
        text1_lbl.place(x=100, y=70)
        text_lbl = Label(window, text="Podaj hasło: ")
        text_lbl.place(x=100, y=90)
        haslo_entry = Entry(window, width=30, show="*")
        haslo_entry.place(x=220, y=90)
        but_wyslij = Button(window, text="Wyślij", bg="#ff9900", command=lambda: verify_and_send_game(haslo_entry.get(), nazwa_gracza, adres_tab, points))
        but_wyslij.place(x=410, y=86)


def verify_and_send_game(password, gracz, adres_t, punkty):

    sciezka_dat = os.path.join(filepath, "xyz\\pass_hash.dat")
    dat_file = open(sciezka_dat, "rb")
    pass_w = pickle.load(dat_file)
    ver_hash = pbkdf2_sha256.verify(password, pass_w)
    dat_file.close()
    if ver_hash:
        tresc = "//:" + gracz + "//:" + punkty
        txid = data_gen.send_lynez_bsv_game(tresc, adres_t)
        if txid:
            msb.showinfo(title="Info", message="Punkty zostały przesłane!\nMożesz zamknąć okno.")
    else:
        msb.showerror(title="Błąd", message="Błędne hasło!")


def notowanie_pkn():

    lista = []
    notowanie = []

    try:
        url_bsv = "https://www.bitcoinsv.pl/6663-2/"
        response_1 = requests.get(url_bsv, timeout=5)
        soup = BeautifulSoup(response_1.content, 'html.parser')
        circle_marq = soup.find_all('h2')
        for i in circle_marq:
            ver = str(i)
            ver_2 = ver[4:].replace("</h2>", "")
            ver_3 = ver_2.split("XX")
            lista.append(ver_3)
    except:
        lista = None
        notowanie = None

    for i in lista:
        q = i[0]
        if q[:3] == "Pkn":
            notowanie.append(i)
    numer_not = notowanie[0]

    return numer_not