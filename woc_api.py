import requests
import pygame
import webbrowser
from bs4 import BeautifulSoup

screen = pygame.display.set_mode((1280, 720))


def test_text(wers, tekst, szerokosc, wysokosc, kolor, rozmiar=24):
    my_font = pygame.font.SysFont("monospace", rozmiar)
    wers = my_font.render(tekst, 1, kolor)
    screen.blit(wers, (szerokosc, wysokosc))


def open_address(adres):

    webbrowser.open("https://whatsonchain.com/address/" + adres)


def test_conn():

    try:
        url_main = "https://api.whatsonchain.com/v1/bsv/main/woc"
        response = requests.get(url_main, timeout=5)
        status_url = response.status_code
    except:
        status_url = 404

    return status_url


def download_pdf(adres):

    webbrowser.open("https://main.whatsonchain.com/statement/" + adres)


def download_tx(txid):

    webbrowser.open("https://main.whatsonchain.com/receipt/" + txid)


def usd_supply():

    try:
        url_1 = "https://api.whatsonchain.com/v1/bsv/main/exchangerate"
        response_1 = requests.get(url_1, timeout=5)
        data = response_1.json()
        rate = data["rate"]
        rate_fl = float(rate)
        rate = round(rate_fl, 2)
        data = str(rate)
        data = data + " $"
    except:
        data = None
        rate_fl = None

    return data, rate_fl


def pln_supply(usd):

    try:
        url_usd = 'http://api.nbp.pl/api/exchangerates/rates/a/usd/'
        response_usd = requests.get(url_usd, timeout=5)
        data_usd = response_usd.json()
        rates = data_usd['rates']
        rates_0 = rates[0]
        mid = rates_0['mid']  # USD/PLN
        pln_x = mid * usd
        pln_t = round(pln_x, 2)
        pln_t = str(pln_t) + " zł"
    except:
        pln_t = None

    return pln_t


def saldo(adres):

    url_1 = "https://api.whatsonchain.com/v1/bsv/main/address/" + adres + "/balance"
    response_1 = requests.get(url_1, timeout=5)
    data = response_1.json()
    confirmed = data["confirmed"]
    ilosc_bsv_i = confirmed / 100000000
    ilosc_bsv_t = str(ilosc_bsv_i)
    ilosc_bsv_t = ilosc_bsv_t + " BSV"

    return ilosc_bsv_t, ilosc_bsv_i


def address_history(adres):

    url_1 = "https://api.whatsonchain.com/v1/bsv/main/address/" + adres + "/history"
    response_1 = requests.get(url_1, timeout=5)
    data = response_1.json()
    try:
        tx_hash = data[:]
        all_tx = len(tx_hash)
        all_tx = str(all_tx)
    except:
        all_tx = "0"

    return all_tx






def bsvpl():

    top_5 = []
    try:
        url_bsv = "https://www.bitcoinsv.pl/"
        response_1 = requests.get(url_bsv, timeout=5)
        soup = BeautifulSoup(response_1.content, 'html.parser')
        circle_marq = soup.find_all('a')
        for i in circle_marq:
            b = i.get("href")
            if len(top_5) != 5:
                if b[30:34] == "2021":
                    top_5.append(b)
                else:
                    continue
            else:
                break

        clean_top_5, a_href_5 = delist(top_5)
    except:
        clean_top_5 = None
        a_href_5 = None

    return clean_top_5, a_href_5


def delist_project():

    try:
        top_3 = bsv_xxx()
        new_top_3 = []
        for i in top_3:
            y = i[4:].replace("</h6>", "")
            z = y.split("XX")
            new_top_3.append(z)
    except:
        new_top_3 = None

    return new_top_3


def bsv_xxx():

    top_3 = []
    try:
        url_bsv = "https://www.bitcoinsv.pl/6663-2/"
        response_1 = requests.get(url_bsv)
        soup = BeautifulSoup(response_1.content, 'html.parser')
        circle_marq = soup.find_all('h6')
        for i in circle_marq:
            top_3.append(str(i))
    except:
        top_3 = None

    return top_3


def hub_version(act_ver):

    try:
        url_bsv = "https://www.bitcoinsv.pl/6663-2/"
        response_1 = requests.get(url_bsv, timeout=5)
        soup = BeautifulSoup(response_1.content, 'html.parser')
        circle_marq = soup.find_all('h3')
        for i in circle_marq:
            ver = str(i)
        version = ver[4:].replace("</h3>", "")
    except:
        version = act_ver

    return version


def konkursy():

    konkursy = []

    try:
        url_bsv = "https://www.bitcoinsv.pl/6663-2/"
        response_1 = requests.get(url_bsv, timeout=5)
        soup = BeautifulSoup(response_1.content, 'html.parser')
        circle_marq = soup.find_all('h4')
        for i in circle_marq:
            ver = str(i)
            ver_2 = ver[4:].replace("</h4>", "")
            ver_3 = ver_2.split("XX")
            konkursy.append(ver_3)
    except:
        konkursy = None

    return konkursy


def best_news():

    best_n = []

    try:
        url_bsv = "https://www.bitcoinsv.pl/6663-2/"
        response_1 = requests.get(url_bsv, timeout=5)
        soup = BeautifulSoup(response_1.content, 'html.parser')
        top_marq = soup.find_all('h5')
        for i in top_marq:
            ver = str(i)
            ver_2 = ver[4:].replace("</h5>", "")
            ver_3 = ver_2.split("XX")
            best_n.append(ver_3)
    except:
        best_n = None

    return best_n


def delist(top_5):

    clean_top_5 = []
    a_href_5 = []

    for i in top_5:
        a_href_5.append(i)
        tytul = i[41:]
        tytul = tytul.replace("-", " ").replace("/", "")
        if len(tytul) > 65:
            tytul = tytul[:65] + ".."
        clean_top_5.append((tytul.title()))

    return clean_top_5, a_href_5


def open_news(link):

    webbrowser.open(link)
