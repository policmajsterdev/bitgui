import os.path
import pygame


pygame.init()
filepath = os.path.dirname(__file__)

#  Grafiki + tła
intro = pygame.image.load(os.path.join(filepath, "z256bg\\bg.png"))
hub_ver_bsv = [pygame.image.load(os.path.join(filepath, "xsys_button\\update_1.png")), pygame.image.load(os.path.join(filepath, "xsys_button\\update_2.png"))]
yt_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_youtube.png"))
discord_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_discord.png"))
website_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_website.png"))
forum_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_forum.png"))
portfel_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_portfel.png"))
kurs_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_kurs.png"))
news_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_news.png"))
gifts_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_gifts.png"))
hub_site = pygame.image.load(os.path.join(filepath, "ws_set\\site_hub.png"))
bg_black = pygame.image.load(os.path.join(filepath, "z256bg\\bg_no_data.png"))
bg_white = pygame.image.load(os.path.join(filepath, "z256bg\\bg_white.png"))
log_bsv = [pygame.image.load(os.path.join(filepath, "xsys_vector\\logos.png")),
      pygame.image.load(os.path.join(filepath, "xsys_vector\\logos1.png"))]

#  Ikona
icon = pygame.image.load(os.path.join(filepath, "z_icon\\bsv.png"))
trophy = [pygame.image.load(os.path.join(filepath, "z_icon\\trophy_1.png")),
          pygame.image.load(os.path.join(filepath, "z_icon\\trophy_2.png")),
          pygame.image.load(os.path.join(filepath, "z_icon\\trophy_3.png"))]

#  Przyciski
ilosc_zgl = pygame.image.load(os.path.join(filepath, "xsys_button\\zgloszenia.png"))
black = pygame.image.load(os.path.join(filepath, "z256bg\\black.png"))
exit_game = pygame.image.load(os.path.join(filepath, "xsys_button\\exit_game.png"))

udzial = [pygame.image.load(os.path.join(filepath, "xsys_button\\udzial_1.png")),
          pygame.image.load(os.path.join(filepath, "xsys_button\\udzial_2.png")),
          pygame.image.load(os.path.join(filepath, "xsys_button\\udzial_3.png"))]

clipboard = [pygame.image.load(os.path.join(filepath, "xsys_button\\clip_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\clip_2.png"))]

add_point = [pygame.image.load(os.path.join(filepath, "xsys_button\\add_point.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\add_point_1.png"))]

game = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_game.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_game_1.png"))]
game_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\game_bg.png"))

gift = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_gift_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_gift_2.png"))]
gift_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\gift_bg.png"))

yt = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_yt_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_yt_2.png"))]
yt_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\yt_bg.png"))

pkn = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_pkn.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_pkn_1.png"))]
pkn_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\pkn_bg.png"))

back = [pygame.image.load(os.path.join(filepath, "xsys_button\\back.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\back1.png"))]

discord = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_ds_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_ds_2.png"))]
discord_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\disc_bg.png"))

website = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_web_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_web_2.png"))]
website_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\web_bg.png"))

kurs = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_kurs_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_kurs_2.png"))]
kurs_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\kurs_bg.png"))

portfel = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_wall_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_wall_2.png"))]
portfel_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\wallet_bg.png"))

forum = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_forum_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_forum_2.png"))]
forum_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\forum_bg.png"))

kick = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_kick_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_kick_2.png"))]
kick_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\kick_bg.png"))

news = [pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_news_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\bsv_news_2.png"))]
news_bg = pygame.image.load(os.path.join(filepath, "xsys_vector\\news_bg.png"))

sound_on = [pygame.image.load(os.path.join(filepath, "xsys_button\\sound_1.png")),
            pygame.image.load(os.path.join(filepath, "xsys_button\\sound_2.png")),
            pygame.image.load(os.path.join(filepath, "xsys_button\\sound_3.png"))]

pdf_button = [pygame.image.load(os.path.join(filepath, "xsys_button\\pdf_1.png")), pygame.image.load(os.path.join(filepath, "xsys_button\\pdf_2.png"))]
chain_button = [pygame.image.load(os.path.join(filepath, "xsys_button\\chain_1.png")), pygame.image.load(os.path.join(filepath, "xsys_button\\chain_2.png"))]

about = [pygame.image.load(os.path.join(filepath, "xsys_button\\about_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\about_2.png"))]

read_more = [pygame.image.load(os.path.join(filepath, "xsys_button\\read_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\read_2.png"))]

arrow_1 = [pygame.image.load(os.path.join(filepath, "xsys_button\\arrow_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\arrow_2.png"))]

arrow_2 = [pygame.image.load(os.path.join(filepath, "xsys_button\\arrow_3.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\arrow_4.png"))]

arrow_3 = [pygame.image.load(os.path.join(filepath, "xsys_button\\arrow_5.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\arrow_6.png"))]

donate = [pygame.image.load(os.path.join(filepath, "xsys_button\\donate_1.png")),
          pygame.image.load(os.path.join(filepath, "xsys_button\\donate_2.png")),
          pygame.image.load(os.path.join(filepath, "xsys_button\\donate_3.png"))]

tdxap = [pygame.image.load(os.path.join(filepath, "xsys_button\\tdxp_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\tdxp_2.png"))]

warunki = [pygame.image.load(os.path.join(filepath, "xsys_button\\warunki_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\warunki_2.png"))]

zebrano = pygame.image.load(os.path.join(filepath, "xsys_button\\zebrano.png"))

#  Otwieranie stron
open_site = [pygame.image.load(os.path.join(filepath, "xsys_button\\open_site_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\open_site_2.png"))]
back_site = [pygame.image.load(os.path.join(filepath, "xsys_vector\\back_button_1.png")),
      pygame.image.load(os.path.join(filepath, "xsys_vector\\back_button_2.png"))]

# PKN
pakano_bg = pygame.image.load(os.path.join(filepath, "pics\\papier_kamien.png"))
papier_wybor = pygame.image.load(os.path.join(filepath, "pics\\papier.png"))
papier_wybor1 = pygame.image.load(os.path.join(filepath, "pics\\papier1.png"))
kamien_wybor = pygame.image.load(os.path.join(filepath, "pics\\kamien.png"))
kamien_wybor1 = pygame.image.load(os.path.join(filepath, "pics\\kamien1.png"))
noz_wybor = pygame.image.load(os.path.join(filepath, "pics\\nozyczki.png"))
noz_wybor1 = pygame.image.load(os.path.join(filepath, "pics\\nozyczki1.png"))
wybor_pc = pygame.image.load(os.path.join(filepath, "pics\\pc_choice.png"))
graj_pkn = [pygame.image.load(os.path.join(filepath, "pics\\play_pkn.png")), pygame.image.load(os.path.join(filepath, "pics\\play_pkn1.png"))]
glass_tv = pygame.image.load(os.path.join(filepath, "pics\\glass_tv.png"))
trophy_pkm = pygame.image.load(os.path.join(filepath, "pics\\trophy.png"))
remis = pygame.image.load(os.path.join(filepath, "pics\\remis.png"))
reset = [pygame.image.load(os.path.join(filepath, "pics\\reset.png")), pygame.image.load(os.path.join(filepath, "pics\\reset1.png"))]
dead = pygame.image.load(os.path.join(filepath, "pics\\dead.png"))
set_point = [pygame.image.load(os.path.join(filepath, "xsys_button\\set_point.png")),
      pygame.image.load(os.path.join(filepath, "xsys_button\\set_point1.png"))]




#  FX
error_woc = pygame.image.load(os.path.join(filepath, "xsys_button\\error_woc.png"))
ok_button = [pygame.image.load(os.path.join(filepath, "xsys_button\\ok.png")), pygame.image.load(os.path.join(filepath, "xsys_button\\ok_2.png"))]


def qr_codex():

    try:
        qr_1 = pygame.image.load(os.path.join(filepath, "qr_code\\main.svg"))
    except FileNotFoundError:
        qr_1 = None
    return qr_1
