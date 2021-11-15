import pickle
import os
import random
import time
from passlib.hash import pbkdf2_sha256
import secrets
import pyperclip
import bitsv

filepath = os.path.dirname(__file__)


# 1 Sprawdza czy istnieją 3 pliki (hasło, klucz, adres)
def check_dat():

    sciezka_dat = os.path.join(filepath, "xyz\\pass_hash.dat")
    sciezka_key = os.path.join(filepath, "xyz\\key_hash.dat")
    sciezka_add = os.path.join(filepath, "xyz\\address.dat")
    try:
        dat_file = open(sciezka_dat, "rb")
        dat_file.close()
        key_file = open(sciezka_key, "rb")
        key_file.close()
        add_file = open(sciezka_add, "rb")
        add_file.close()
        file = True
    except FileNotFoundError:
        file = None
    return file


# 2 Tworzy, weryfikuje hasło i skrót
def verify_hash(new_pass):

    new_hash = pbkdf2_sha256.hash(new_pass)
    ver_hash = pbkdf2_sha256.verify(new_pass, new_hash)
    if ver_hash:
        pickle_dat(new_hash)
    else:
        pass


# 3 Tworzy plik z hasłem, tworzy klucz prywatny
def pickle_dat(hashs):

    sciezka_dat = os.path.join(filepath, "xyz\\pass_hash.dat")
    new_file_dat = open(sciezka_dat, "wb")
    pickle.dump(hashs, new_file_dat)
    new_file_dat.close()
    p_key = gen_key()
    sciezka_key = os.path.join(filepath, "xyz\\key_hash.dat")
    new_file_key = open(sciezka_key, "wb")
    pickle.dump(p_key, new_file_key)
    new_file_key.close()


# 4 Tworzy klucz prywatny
def gen_key():

    bits = secrets.randbits(256)
    bits_hex = hex(bits)
    private_key = bits_hex[2:]
    while len(private_key) != 64:
        private_key = gen_key()
    set_add(private_key)
    new_private_key = numeaire(private_key)
    return new_private_key


# 5 Tworzy plik z adresem publicznym
def set_add(bsvkey):

    demo_public_add = bitsv.Key.from_hex(bsvkey, network="main")
    public_add = demo_public_add.address
    sciezka_add = os.path.join(filepath, "xyz\\address.dat")
    new_file_add = open(sciezka_add, "wb")
    pickle.dump(public_add, new_file_add)
    new_file_add.close()


# Szyfruje klucz prywatny
def numeaire(num_bits):

    new_bit = ""
    alphabet = "abcdef1234567890"
    seed = ""
    while len(seed) != 12:
        rand = random.randrange(15)
        seed += alphabet[rand]

    end = len(num_bits)
    for i in range(len(num_bits)):
        new_bit += num_bits[i] + num_bits[end - 1]
        end -= 1
    beautiful_hash = seed[:5] + new_bit[:64] + seed[6:]
    return beautiful_hash


# Otwiera plik o odczytuje adres publiczny
def open_address():

    try:
        sciezka_add = os.path.join(filepath, "xyz\\address.dat")
        add_file = open(sciezka_add, "rb")
        sh_add = pickle.load(add_file)
        add_file.close()
    except FileNotFoundError:
        sh_add = None
    return sh_add


def send_bsv(ilosc, adres):

    qr_pass = open_pass()
    my_key = bitsv.Key.from_hex(qr_pass, network="main")
    ilosc = float(ilosc)
    out_put = [(adres, ilosc, 'bsv')]
    tx = my_key.send(out_put)
    time.sleep(2)
    if tx:
        txi = True
    else:
        txi = False
    return txi


def send_gift_bsv(tresc, adres):

    qr_pass = open_pass()
    my_key = bitsv.Key.from_hex(qr_pass, network="main")
    out_put = [(adres, '0.00000001', 'bsv')]
    tx = my_key.send(out_put, message=tresc, custom_pushdata=False)
    time.sleep(2)
    if tx:
        txi = True
    else:
        txi = False
    return txi


def send_lynez_bsv_game(tresc, adres):

    qr_pass = open_pass()
    my_key = bitsv.Key.from_hex(qr_pass, network="main")
    out_put = [(adres, '0.0002', 'bsv')]
    tx = my_key.send(out_put, message=tresc, custom_pushdata=False)
    time.sleep(2)
    if tx:
        txi = True
    else:
        txi = False
    return txi


def open_pass():

    sciezka_pass = os.path.join(filepath, "xyz\\key_hash.dat")
    pass_file = open(sciezka_pass, "rb")
    pass_w = pickle.load(pass_file)
    if pass_w:
        enc_bit = integrai(pass_w)
    else:
        enc_bit = None

    return enc_bit


# Odszyfrowuje
def integrai(new_bit):

    f_blank = new_bit[5:-6]
    blank = f_blank[::-1]
    b_lst = f_blank + blank
    enc_bit = ""
    start = 0
    for i in range(len(b_lst)):
        if (i + start) < len(b_lst):
            enc_bit += b_lst[i + start]
            if (i + start) >= len(b_lst):
                break
            else:
                start += 1
    return enc_bit


# Kopiuje tekst do schowka
def copy_to_clip(text):

    pyperclip.copy(text)
