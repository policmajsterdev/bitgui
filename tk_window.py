import os
import pickle
from tkinter import *
from tkinter import messagebox as msb
from passlib.hash import pbkdf2_sha256
import data_gen

filepath = os.path.dirname(__file__)


def przelicz_bsv(kwota):

    wynik = int(kwota) / 100000000
    wynik_1 = "{:.8f}".format(wynik)
    wynik_str = "Wysyłasz " + str(wynik_1) + " BSV"

    return wynik_1, wynik_str


def verify_and_send(haslo, ilosc, adres):

    sciezka_dat = os.path.join(filepath, "xyz\\pass_hash.dat")
    dat_file = open(sciezka_dat, "rb")
    pass_w = pickle.load(dat_file)
    ver_hash = pbkdf2_sha256.verify(haslo, pass_w)
    dat_file.close()
    if ver_hash:
        txid = data_gen.send_bsv(ilosc, adres)
        if txid:
            msb.showinfo(title="Info", message="Transakcja została wykonana!\nMożesz zamknąć okno dotacji.")
    else:
        msb.showerror(title="Błąd", message="Błędne hasło!")


def dalej_2(kwota, window, adres):

    if not kwota or kwota == "0":
        msb.showwarning(title="Błąd", message="Nie możesz wysłać 0 sat.")
    else:
        check_n = dalej_1(kwota)
        if not check_n:
            pass
        else:
            ile_bsv, ile_bsv_str = przelicz_bsv(kwota)
            text1_lbl = Label(window, text=ile_bsv_str, fg="#006666")
            text1_lbl.place(x=100, y=70)
            text_lbl = Label(window, text="Podaj hasło: ")
            text_lbl.place(x=100, y=90)
            haslo_entry = Entry(window, width=30, show="*")
            haslo_entry.place(x=220, y=90)
            but_wyslij = Button(window, text="Wyślij", bg="#ff9900", command=lambda: verify_and_send(haslo_entry.get(), ile_bsv, adres))
            but_wyslij.place(x=410, y=86)


def dalej_1(kwota):

    check_n = None

    for i in kwota:
        check_number = i.isnumeric()
        if check_number:
            check_n = True
        else:
            msb.showwarning(title="Błąd", message="Zamiast kwoty podałeś literę.")
            check_n = None

    return check_n


def window_transfer(projekt, adres):

    wstep = "Wsparcie dla " + projekt
    adresik = adres
    root = Tk()
    root.geometry("500x200")
    root.title(wstep)

    # Buttony
    text1_lbl = Label(root, text="Jeśli chcesz wysłać np. 0,00000100 BSV - wpisz 100", fg="#006666")
    text1_lbl.place(x=100, y=10)

    text_lbl = Label(root, text="Podaj ilość satoshi: ")
    text_lbl.place(x=100, y=50)

    kwota_entry = Entry(root, width=30)
    kwota_entry.place(x=220, y=50)

    but_dalej = Button(root, text="Dalej", bg="#009900", command=lambda: dalej_2(kwota_entry.get(), root, adresik))
    but_dalej.place(x=410, y=46)

    root.mainloop()
