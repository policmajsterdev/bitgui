import pyqrcode
import os

filepath = os.path.dirname(__file__)


def check_main_qr():

    sciezka_main = os.path.join(filepath, "qr_code\\main.svg")
    try:
        dat_file = open(sciezka_main)
        dat_file.close()
        qr_file = True
    except FileNotFoundError:
        qr_file = None

    return qr_file


def create_qrcode(adres):

    qradres = pyqrcode.create(adres)
    file = os.path.join(filepath, "qr_code\\main.svg")
    qradres.svg(file, scale=4)
