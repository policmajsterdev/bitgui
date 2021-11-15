import os
import pickle
from tkinter import *
from tkinter import messagebox as msb
from passlib.hash import pbkdf2_sha256
import data_gen
import check_txid

filepath = os.path.dirname(__file__)


def verify_and_send(haslo, tresc, adres):

    sciezka_dat = os.path.join(filepath, "xyz\\pass_hash.dat")
    dat_file = open(sciezka_dat, "rb")
    pass_w = pickle.load(dat_file)
    ver_hash = pbkdf2_sha256.verify(haslo, pass_w)
    dat_file.close()
    if ver_hash:
        txid = data_gen.send_gift_bsv(tresc, adres)
        if txid:
            msb.showinfo(title="Info", message="Wiadomość została wysłana!\nMożesz zamknąć okno.")
    else:
        msb.showerror(title="Błąd", message="Błędne hasło!")


def dalej_2(tresc, window, adres):

    if not tresc:
        msb.showwarning(title="Błąd", message="Nie możesz wysłać pustej wiadomości.")
    else:
        text1_lbl = Label(window, text=tresc, fg="#006666")
        text1_lbl.place(x=100, y=70)
        text_lbl = Label(window, text="Podaj hasło: ")
        text_lbl.place(x=100, y=90)
        haslo_entry = Entry(window, width=30, show="*")
        haslo_entry.place(x=220, y=90)
        but_wyslij = Button(window, text="Wyślij", bg="#ff9900", command=lambda: verify_and_send(haslo_entry.get(), tresc, adres))
        but_wyslij.place(x=410, y=86)


def window_gift_send(projekt, adres):

    wstep = "Udział w konkursie: " + projekt
    root = Tk()
    root.geometry("500x200")
    root.title(wstep)

    # Buttony

    text1_lbl = Label(root, text="Za chwilę wyślesz wiadomość do blockchain BSV! ♡", fg="#006666")
    text1_lbl.place(x=120, y=10)

    text_lbl = Label(root, text="Wpisz treść do wysłania: ")
    text_lbl.place(x=80, y=50)

    tresc_entry = Entry(root, width=30)
    tresc_entry.place(x=220, y=50)

    but_dalej = Button(root, text="Dalej", bg="#009900", command=lambda: dalej_2(tresc_entry.get(), root, adres))
    but_dalej.place(x=410, y=46)

    text2_lbl = Label(root, text="Zero ukrytych opłat! :)", fg="#008080")
    text2_lbl.place(x=10, y=130)
    text3_lbl = Label(root, text="☆  0.00000001 BSV przesyłasz na adres konkursowy", fg="#008080")
    text3_lbl.place(x=20, y=150)
    text4_lbl = Label(root, text="☆  0.00000250 BSV przesyłasz górnikowi by potwierdzić transkację", fg="#008080")
    text4_lbl.place(x=20, y=170)

    root.mainloop()


def verify_and_send_pkn(haslo, ilosc, adres):

    sciezka_dat = os.path.join(filepath, "xyz\\pass_hash.dat")
    dat_file = open(sciezka_dat, "rb")
    pass_w = pickle.load(dat_file)
    ver_hash = pbkdf2_sha256.verify(haslo, pass_w)
    dat_file.close()
    if ver_hash:
        txid = data_gen.send_bsv(ilosc, adres)
        if txid:
            check_txid.check_txid_game(txid)
            msb.showinfo(title="Info", message="Transakcja została wykonana!\nZamknij okno i wejdź do gry :)")
    else:
        msb.showerror(title="Błąd", message="Błędne hasło!")


def enter_game_password(window, adres_gry):

        ilosc = "0.0002"
        text_lbl = Label(window, text="Podaj hasło: ")
        text_lbl.place(x=100, y=120)
        haslo_entry = Entry(window, width=30, show="*")
        haslo_entry.place(x=190, y=120)
        but_wyslij = Button(window, text="Wyślij", bg="#ff9900", command=lambda: verify_and_send_pkn(haslo_entry.get(), ilosc, adres_gry))
        but_wyslij.place(x=410, y=116)


def enter_game(adres_gry):

    wstep = "Wejście by grać o BSV jest płatne - 0.0002 BSV"
    root = Tk()
    root.geometry("500x200")
    root.title(wstep)

    # Buttony

    text1_lbl = Label(root, text="☆ Płacisz 1 raz i grasz do woli! ☆", fg="#006666")
    text1_lbl.place(x=190, y=5)
    text1_lb2 = Label(root, text="☆ Wpiszesz się jeśli zdobędziesz satysfakcjonujący Cię wynik! ☆", fg="#006666")
    text1_lb2.place(x=110, y=22)

    text_lbl = Label(root, text="☆ Z Twojego portfela zostanie pobrane 0.0002 BSV ☆")
    text_lbl.place(x=135, y=50)

    but_dalej = Button(root, text="Wchodzę i gram", bg="#009900", command=lambda: enter_game_password(root, adres_gry))
    but_dalej.place(x=230, y=80)
    root.mainloop()


def empty_bsv():

    wstep = "Hola, hola!"
    root = Tk()
    root.geometry("500x200")
    root.title(wstep)

    # Buttony

    text1_lbl = Label(root, text="☆ Płacisz 1 raz i grasz do woli! ☆", fg="#006666")
    text1_lbl.place(x=170, y=5)
    text1_lb2 = Label(root, text="☆ Wpiszesz się jeśli zdobędziesz satysfakcjonujący Cię wynik! ☆", fg="#006666")
    text1_lb2.place(x=90, y=22)

    text_lbl = Label(root, text="☆ Z Twojego portfela zostanie pobrane 0.0002 BSV ☆")
    text_lbl.place(x=115, y=50)

    but_dalej = Label(root, text="Nie masz BSV na wejście.. :(", bg="#ff3333")
    but_dalej.place(x=195, y=80)
    root.mainloop()
