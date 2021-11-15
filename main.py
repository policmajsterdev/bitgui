import pygame
import sys
import random
import webbrowser

import check_txid
import data_gen
import images_bsv
import qr_code
import tk_window
import tk_window_gift
import woc_api
import lynez_conf
import pkn_conf
import data.entities as e
import data.lines as line_math
import data.text as text
from data.core_funcs import *
from pygame.locals import *


#  HUB Version
hub_ver = "0.3"

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

filepath = os.path.dirname(__file__)
myFont = pygame.font.SysFont("monospace", 18)
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(32)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("HubSV - bitcoin sv Polska")
mainClock = pygame.time.Clock()
pygame.display.set_icon(images_bsv.icon)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 204, 0)
gold = (204, 153, 0)
bronze = (204, 102, 0)
grey = (166, 166, 166)
controlVol = 0.5
click_wav = pygame.mixer.Sound(os.path.join(filepath, "wd_sdn16\\click.wav"))
click_b_wav = pygame.mixer.Sound(os.path.join(filepath, "wd_sdn16\\click_b.wav"))
main_intro = pygame.mixer.Sound(os.path.join(filepath, "wd_sdn16\\main_intro.ogg"))
pygame.mixer.music.load(os.path.join(filepath, "wd_sdn16\\intro_music.ogg"))
game_lyn = pygame.mixer.Sound(os.path.join(filepath, "wd_sdn16\\game.ogg"))
pkn_wav = pygame.mixer.Sound(os.path.join(filepath, "wd_sdn16\\pkn.ogg"))
win = pygame.mixer.Sound(os.path.join(filepath, "wd_sdn16\\win.wav"))
lose = pygame.mixer.Sound(os.path.join(filepath, "wd_sdn16\\lose.wav"))
pygame.mixer.music.set_volume(controlVol)
user_text = ""
particlesZ = []
BORDER_WIDTH = 70
display = pygame.Surface((275, 400))
gui_display = pygame.Surface((275, 400))
gui_display.set_colorkey((0, 0, 0))
e.load_particle_images('data/images/particles')
e.set_global_colorkey((0, 0, 0))
font = text.Font('data/fonts/large_font.png', (255, 255, 255))
font2 = text.Font('data/fonts/large_font.png', (0, 0, 1))
bounce_s = pygame.mixer.Sound('data/sfx/bounce.wav')
death_s = pygame.mixer.Sound('data/sfx/death.wav')
laser_charge_s = pygame.mixer.Sound('data/sfx/laser_charge.wav')
laser_explode_s = pygame.mixer.Sound('data/sfx/laser_explode.wav')
place_s = pygame.mixer.Sound('data/sfx/place.wav')
restart_s = pygame.mixer.Sound('data/sfx/restart.wav')
bounce_s.set_volume(0.7)
place_s.set_volume(0.9)
laser_charge_s.set_volume(0.05)
background_color = (13, 20, 33)
background_polygon_color = (24, 34, 46)
line_color = (255, 255, 255)
line_placing_color = (90, 140, 170)
line_width = 3
player_color = (90, 210, 255)
player_gravity = 0.05
player_terminal_velocity = 1
bounce_strength = 1
game_score = 0
txid = None


def volume_0():
    global controlVol
    pygame.mixer.music.pause()
    controlVol = 0.0
    pygame.mixer.Sound.set_volume(click_wav, 0.0)
    pygame.mixer.Sound.set_volume(click_b_wav, 0.0)
    pygame.mixer.Sound.set_volume(main_intro, 0.0)


def volume_1():
    global controlVol
    pygame.mixer.music.pause()
    controlVol = 0.5
    pygame.mixer.Sound.set_volume(click_wav, 0.5)
    pygame.mixer.Sound.set_volume(click_b_wav, 0.5)
    pygame.mixer.Sound.set_volume(main_intro, 0.5)


def hubsv_menu(version_hub):
    global txid
    main_intro.play(-1)
    rgb = (255, 255, 255)
    update_version = woc_api.hub_version(version_hub)
    numer_notowania, adres_tablicy = pkn_conf.notowanie_pkn()
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.intro, (0, 0))

        yt_0 = screen.blit(images_bsv.yt[0], (392, 615))
        disc_0 = screen.blit(images_bsv.discord[0], (265, 462))
        web_0 = screen.blit(images_bsv.website[0], (463, 427))
        kurs_0 = screen.blit(images_bsv.kurs[0], (198, 190))
        wall_0 = screen.blit(images_bsv.portfel[0], (399, 237))
        forum_0 = screen.blit(images_bsv.forum[0], (596, 280))
        kick_0 = screen.blit(images_bsv.kick[0], (401, 46))
        news_0 = screen.blit(images_bsv.news[0], (600, 51))
        gift_0 = screen.blit(images_bsv.gift[0], (264, 308))
        logos_0 = screen.blit(images_bsv.log_bsv[0], (490, 625))
        game_0 = screen.blit(images_bsv.game[0], (190, 574))
        game_2 = screen.blit(images_bsv.pkn[0], (124, 457))

        #  Update
        if version_hub != update_version:
            ver_0 = screen.blit(images_bsv.hub_ver_bsv[0], (930, 10))
            if ver_0.collidepoint((mx, my)):
                screen.blit(images_bsv.hub_ver_bsv[1], (930, 10))
                if click:
                    open_version()
        # Close update

        # Sound
        if controlVol == 0.5:
            sound_0 = screen.blit(images_bsv.sound_on[0], (1200, 10))
            if sound_0.collidepoint((mx, my)):
                screen.blit(images_bsv.sound_on[1], (1200, 10))
                if click:
                    click_wav.play()
                    volume_0()
        else:
            sound_0 = screen.blit(images_bsv.sound_on[2], (1200, 10))
            if sound_0.collidepoint((mx, my)):
                screen.blit(images_bsv.sound_on[1], (1200, 10))
                if click:
                    click_wav.play()
                    volume_1()
        # Close sound

        if game_2.collidepoint((mx, my)):
            rgb = (0, 255, 0)
            screen.blit(images_bsv.pkn[1], (124, 457))
            screen.blit(images_bsv.pkn_bg, (887, 0))
            if click:
                click_wav.play()
                if not txid:
                    status_woc = woc_api.test_conn()
                    if status_woc == 200:
                        adres = data_gen.open_address()
                        saldo_main = woc_api.saldo(adres)
                        if saldo_main[1] > 0.0003:
                            tk_window_gift.enter_game(adres_tablicy)
                            txid = check_txid.send_txid()
                        else:
                            tk_window_gift.empty_bsv()
                else:
                    main_intro.stop()
                    papier()
        if yt_0.collidepoint((mx, my)):
            rgb = (0, 0, 0)
            screen.blit(images_bsv.yt[1], (392, 615))
            screen.blit(images_bsv.yt_bg, (887, 0))
            if click:
                click_wav.play()
                youtube_site()
        if disc_0.collidepoint((mx, my)):
            rgb = (0, 102, 0)
            screen.blit(images_bsv.discord[1], (265, 462))
            screen.blit(images_bsv.discord_bg, (887, 0))
            if click:
                click_wav.play()
                discord_site()
        if web_0.collidepoint((mx, my)):
            rgb = (102, 0, 204)
            screen.blit(images_bsv.website[1], (463, 427))
            screen.blit(images_bsv.website_bg, (887, 0))
            if click:
                click_wav.play()
                website_site()
        if kurs_0.collidepoint((mx, my)):
            rgb = (204, 153, 0)
            screen.blit(images_bsv.kurs[1], (198, 190))
            screen.blit(images_bsv.kurs_bg, (887, 0))
            if click:
                click_wav.play()
                kurs_site()
        if wall_0.collidepoint((mx, my)):
            rgb = (255, 255, 255)
            screen.blit(images_bsv.portfel[1], (399, 237))
            screen.blit(images_bsv.portfel_bg, (887, 0))
            if click:
                click_wav.play()
                wallet_site()
        if forum_0.collidepoint((mx, my)):
            rgb = (0, 0, 102)
            screen.blit(images_bsv.forum[1], (596, 280))
            screen.blit(images_bsv.forum_bg, (887, 0))
            if click:
                click_wav.play()
                forum_site()
        if kick_0.collidepoint((mx, my)):
            rgb = (153, 102, 0)
            screen.blit(images_bsv.kick[1], (401, 46))
            screen.blit(images_bsv.kick_bg, (887, 0))
            if click:
                click_wav.play()
                hub_site()
        if news_0.collidepoint((mx, my)):
            rgb = (51, 153, 51)
            screen.blit(images_bsv.news[1], (600, 51))
            screen.blit(images_bsv.news_bg, (887, 0))
            if click:
                click_wav.play()
                news_site()
        if game_0.collidepoint((mx, my)):
            rgb = (204, 204, 0)
            screen.blit(images_bsv.game[1], (190, 574))
            screen.blit(images_bsv.game_bg, (887, 0))
            if click:
                main_intro.stop()
                click_wav.play()
                game_Lynez()
        if gift_0.collidepoint((mx, my)):
            rgb = (204, 0, 102)
            screen.blit(images_bsv.gift[1], (264, 308))
            screen.blit(images_bsv.gift_bg, (887, 0))
            if click:
                click_wav.play()
                gift_site()
        if logos_0.collidepoint((mx, my)):
            screen.blit(images_bsv.log_bsv[1], (490, 625))

        particlesZ.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 5)])
        for particle in particlesZ:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.05
            particle[1][1] += 0.1
            pygame.draw.circle(screen, rgb, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particlesZ.remove(particle)

        pygame.display.update()
        mainClock.tick(40)


def gift_site():
    saldo_main = None
    konkursy = woc_api.konkursy()
    if konkursy:
        status_woc = woc_api.test_conn()
        adres = data_gen.open_address()
        zgloszenia = woc_api.address_history(konkursy[0][8])
        if status_woc == 200:
            saldo_main = woc_api.saldo(adres)
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.gifts_site, (0, 0))

        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))
        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break
        if konkursy:
            woc_api.test_text("tytul", konkursy[0][0], 260, 174, white, 24)
            woc_api.test_text("tytul1", konkursy[0][1], 260, 214, white, 18)
            woc_api.test_text("tytul2", konkursy[0][2], 260, 244, white, 18)
            woc_api.test_text("tytul3", konkursy[0][3], 260, 274, white, 18)
            woc_api.test_text("tytul4", konkursy[0][4], 260, 304, white, 18)
            woc_api.test_text("tytul5", konkursy[0][5], 260, 334, white, 18)
            woc_api.test_text("tytul6", konkursy[0][6], 260, 364, white, 18)
            open_site = screen.blit(images_bsv.warunki[0], (260, 400))
            if open_site.collidepoint((mx, my)):
                screen.blit(images_bsv.warunki[1], (260, 400))
                if click:
                    click_b_wav.play()
                    woc_api.open_news(konkursy[0][7])

            if saldo_main[1] != 0:
                udzial_0 = screen.blit(images_bsv.udzial[0], (260, 500))
                if udzial_0.collidepoint((mx, my)):
                    screen.blit(images_bsv.udzial[1], (260, 500))
                    if click:
                        click_b_wav.play()
                        tk_window_gift.window_gift_send(konkursy[0][0], konkursy[0][8])

            else:
                screen.blit(images_bsv.udzial[2], (260, 500))
                woc_api.test_text("ilosc", "Nie możesz brać udziału w konkursie? Zasil swój portfel!", 260, 550, white, 17)

            screen.blit(images_bsv.ilosc_zgl, (460, 500))
            woc_api.test_text("ilosc", str(zgloszenia), 673, 508, white, 17)

        else:
            woc_api.test_text("brak", "Aktualnie brak konkursów. Wróc za jakiś czas :)", 260, 174, white, 24)

        pygame.display.update()
        mainClock.tick(30)


def youtube_site():
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.yt_site, (0, 0))

        yt_1 = screen.blit(images_bsv.open_site[0], (900, 520))
        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))

        if yt_1.collidepoint((mx, my)):
            screen.blit(images_bsv.open_site[1], (900, 520))
            if click:
                open_yt()
        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break

        pygame.display.update()
        mainClock.tick(30)


def kurs_site():
    usd = None
    pln = None
    status_woc = woc_api.test_conn()
    if status_woc == 200:
        usd, rate_float = woc_api.usd_supply()
        pln = woc_api.pln_supply(rate_float)
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.kurs_site, (0, 0))

        if status_woc != 200:
            screen.blit(images_bsv.error_woc, (800, 160))
        else:
            woc_api.test_text("usd", usd, 860, 207, white, 30)
            woc_api.test_text("pln", pln, 860, 347, white, 30)

        if not pln:
            screen.blit(images_bsv.error_woc, (830, 330))

        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))
        tdx_1 = screen.blit(images_bsv.tdxap[0], (400, 523))

        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break
        if tdx_1.collidepoint((mx, my)):
            screen.blit(images_bsv.tdxap[1], (400, 523))
            if click:
                click_wav.play()
                open_tdxp()

        pygame.display.update()
        mainClock.tick(30)


def discord_site():
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.discord_site, (0, 0))

        disc_1 = screen.blit(images_bsv.open_site[0], (900, 520))
        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))

        if disc_1.collidepoint((mx, my)):
            screen.blit(images_bsv.open_site[1], (900, 520))
            if click:
                open_discord()
        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break

        pygame.display.update()
        mainClock.tick(30)


def website_site():
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.website_site, (0, 0))

        web_1 = screen.blit(images_bsv.open_site[0], (900, 520))
        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))

        if web_1.collidepoint((mx, my)):
            screen.blit(images_bsv.open_site[1], (900, 520))
            if click:
                open_bsvpl()
        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break

        pygame.display.update()
        mainClock.tick(30)


def hub_site():
    saldo_main = None
    saldo_projekt_1 = None
    saldo_projekt_2 = None
    saldo_projekt_3 = None
    top3_projects = woc_api.delist_project()
    status_woc = woc_api.test_conn()
    adres = data_gen.open_address()
    if status_woc == 200:
        saldo_main = woc_api.saldo(adres)
    if top3_projects:
        if len(top3_projects) >= 1:
            saldo_projekt_1 = woc_api.saldo(top3_projects[0][6])
        if len(top3_projects) >= 2:
            saldo_projekt_2 = woc_api.saldo(top3_projects[1][6])
        if len(top3_projects) >= 3:
            saldo_projekt_3 = woc_api.saldo(top3_projects[2][6])
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.hub_site, (0, 0))

        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))
        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break

        if len(top3_projects) >= 1:
            screen.blit(images_bsv.zebrano, (490, 267))
            woc_api.test_text("2zebrano", saldo_projekt_1[0], 610, 272, white, 18)
            woc_api.test_text("1nazwa", str(top3_projects[0][0]), 400, 150, white, 21)
            woc_api.test_text("1opis1", str(top3_projects[0][2]), 400, 183, white, 15)
            woc_api.test_text("1opis2", str(top3_projects[0][3]), 400, 203, white, 15)
            woc_api.test_text("1opis3", str(top3_projects[0][4]), 400, 223, white, 15)
            woc_api.test_text("1opis4", str(top3_projects[0][5]), 400, 243, white, 15)
            t_new1 = screen.blit(images_bsv.arrow_1[0], (1100, 146))
            if t_new1.collidepoint((mx, my)):
                screen.blit(images_bsv.arrow_1[1], (1100, 146))
                if click:
                    woc_api.open_news(top3_projects[0][1])

            if saldo_main[1] != 0:
                donate_1 = screen.blit(images_bsv.donate[0], (394, 265))
                if donate_1.collidepoint((mx, my)):
                    screen.blit(images_bsv.donate[1], (394, 265))
                    if click:
                        tk_window.window_transfer(str(top3_projects[0][0]), top3_projects[0][6])
            else:
                screen.blit(images_bsv.donate[2], (394, 265))

        if len(top3_projects) >= 2:
            screen.blit(images_bsv.zebrano, (490, 437))
            woc_api.test_text("2zebrano", saldo_projekt_2[0], 610, 442, white, 18)
            woc_api.test_text("2nazwa", str(top3_projects[1][0]), 400, 320, white, 21)
            woc_api.test_text("2opis1", str(top3_projects[1][2]), 400, 353, white, 15)
            woc_api.test_text("2opis2", str(top3_projects[1][3]), 400, 373, white, 15)
            woc_api.test_text("2opis3", str(top3_projects[1][4]), 400, 393, white, 15)
            woc_api.test_text("2opis4", str(top3_projects[1][5]), 400, 413, white, 15)
            t_new2 = screen.blit(images_bsv.arrow_2[0], (1100, 316))
            if t_new2.collidepoint((mx, my)):
                screen.blit(images_bsv.arrow_2[1], (1100, 316))
                if click:
                    woc_api.open_news(top3_projects[1][1])

            if saldo_main[1] != 0:
                donate_2 = screen.blit(images_bsv.donate[0], (394, 435))
                if donate_2.collidepoint((mx, my)):
                    screen.blit(images_bsv.donate[1], (394, 435))
                    if click:
                        tk_window.window_transfer(str(top3_projects[1][0]), top3_projects[1][6])
            else:
                screen.blit(images_bsv.donate[2], (394, 435))

        if len(top3_projects) >= 3:
            screen.blit(images_bsv.zebrano, (490, 607))
            woc_api.test_text("3zebrano", saldo_projekt_3[0], 610, 612, white, 18)
            woc_api.test_text("3nazwa", str(top3_projects[2][0]), 400, 490, white, 21)
            woc_api.test_text("3opis1", str(top3_projects[2][2]), 400, 523, white, 15)
            woc_api.test_text("3opis2", str(top3_projects[2][3]), 400, 543, white, 15)
            woc_api.test_text("3opis3", str(top3_projects[2][4]), 400, 563, white, 15)
            woc_api.test_text("3opis4", str(top3_projects[2][5]), 400, 583, white, 15)
            t_new2 = screen.blit(images_bsv.arrow_3[0], (1100, 486))
            if t_new2.collidepoint((mx, my)):
                screen.blit(images_bsv.arrow_3[1], (1100, 486))
                if click:
                    woc_api.open_news(top3_projects[2][1])

            if saldo_main[1] != 0:
                donate_2 = screen.blit(images_bsv.donate[0], (394, 605))
                if donate_2.collidepoint((mx, my)):
                    screen.blit(images_bsv.donate[1], (394, 605))
                    if click:
                        tk_window.window_transfer(str(top3_projects[2][0]), top3_projects[2][6])
            else:
                screen.blit(images_bsv.donate[2], (394, 605))

        if len(top3_projects) == 0:
            screen.blit(images_bsv.error_woc, (710, 190))

        pygame.display.update()
        mainClock.tick(30)


def forum_site():
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.forum_site, (0, 0))

        for_1 = screen.blit(images_bsv.open_site[0], (900, 520))
        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))

        if for_1.collidepoint((mx, my)):
            screen.blit(images_bsv.open_site[1], (900, 520))
            if click:
                open_forum()
        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break

        pygame.display.update()
        mainClock.tick(30)


def news_site():
    top_5, href_5 = woc_api.bsvpl()
    best_news = woc_api.best_news()
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.news_site, (0, 0))

        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))
        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break
        if top_5:
            woc_api.test_text("1", "1. " + top_5[0], 390, 177, white, 17)
            woc_api.test_text("2", "2. " + top_5[1], 390, 217, white, 17)
            woc_api.test_text("3", "3. " + top_5[2], 390, 257, white, 17)
            woc_api.test_text("4", "4. " + top_5[3], 390, 297, white, 17)
            woc_api.test_text("5", "5. " + top_5[4], 390, 337, white, 17)

            news_1 = screen.blit(images_bsv.read_more[0], (1120, 172))
            if news_1.collidepoint((mx, my)):
                screen.blit(images_bsv.read_more[1], (1120, 172))
                if click:
                    woc_api.open_news(href_5[0])
            news_2 = screen.blit(images_bsv.read_more[0], (1120, 212))
            if news_2.collidepoint((mx, my)):
                screen.blit(images_bsv.read_more[1], (1120, 212))
                if click:
                    woc_api.open_news(href_5[1])
            news_3 = screen.blit(images_bsv.read_more[0], (1120, 252))
            if news_3.collidepoint((mx, my)):
                screen.blit(images_bsv.read_more[1], (1120, 252))
                if click:
                    woc_api.open_news(href_5[2])
            news_4 = screen.blit(images_bsv.read_more[0], (1120, 292))
            if news_4.collidepoint((mx, my)):
                screen.blit(images_bsv.read_more[1], (1120, 292))
                if click:
                    woc_api.open_news(href_5[3])
            news_5 = screen.blit(images_bsv.read_more[0], (1120, 332))
            if news_5.collidepoint((mx, my)):
                screen.blit(images_bsv.read_more[1], (1120, 332))
                if click:
                    woc_api.open_news(href_5[4])
        else:
            screen.blit(images_bsv.error_woc, (700, 240))

        if best_news:
            woc_api.test_text("1", "1. " + best_news[0][0], 390, 507, white, 17)
            woc_api.test_text("2", "2. " + best_news[1][0], 390, 547, white, 17)
            woc_api.test_text("3", "3. " + best_news[2][0], 390, 587, white, 17)

            best_1 = screen.blit(images_bsv.read_more[0], (1120, 502))
            if best_1.collidepoint((mx, my)):
                screen.blit(images_bsv.read_more[1], (1120, 502))
                if click:
                    woc_api.open_news(best_news[0][1])

            best_2 = screen.blit(images_bsv.read_more[0], (1120, 542))
            if best_2.collidepoint((mx, my)):
                screen.blit(images_bsv.read_more[1], (1120, 542))
                if click:
                    woc_api.open_news(best_news[1][1])

            best_3 = screen.blit(images_bsv.read_more[0], (1120, 582))
            if best_3.collidepoint((mx, my)):
                screen.blit(images_bsv.read_more[1], (1120, 582))
                if click:
                    woc_api.open_news(best_news[2][1])
        else:
            screen.blit(images_bsv.error_woc, (700, 530))

        pygame.display.update()
        mainClock.tick(30)


def wallet_site():
    saldo_main = None
    all_txid = None
    status_woc = woc_api.test_conn()
    adres = data_gen.open_address()
    qr_main = qr_code.check_main_qr()
    if not qr_main:
        qr_code.create_qrcode(adres)
    if status_woc == 200:
        saldo_main = woc_api.saldo(adres)
        all_txid = woc_api.address_history(adres)
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.portfel_site, (0, 0))

        back_1 = screen.blit(images_bsv.back_site[0], (0, 0))
        if back_1.collidepoint((mx, my)):
            screen.blit(images_bsv.back_site[1], (0, 0))
            if click:
                click_b_wav.play()
                break

        if status_woc != 200:
            screen.blit(images_bsv.error_woc, (800, 160))
        else:
            woc_api.test_text("saldo", saldo_main[0], 760, 174, white)
            woc_api.test_text("adres", adres, 760, 240, white, 19)
            woc_api.test_text("trans", all_txid, 760, 306, white)

            chain_click = screen.blit(images_bsv.chain_button[0], (510, 522))
            if chain_click.collidepoint((mx, my)):
                screen.blit(images_bsv.chain_button[1], (510, 522))
                if click:
                    woc_api.open_address(adres)

            if int(all_txid) > 0:
                pdf_click = screen.blit(images_bsv.pdf_button[0], (380, 540))
                if pdf_click.collidepoint((mx, my)):
                    screen.blit(images_bsv.pdf_button[1], (380, 540))
                    if click:
                        woc_api.download_pdf(adres)

            clip_0 = screen.blit(images_bsv.clipboard[0], (1155, 236))
            if clip_0.collidepoint((mx, my)):
                screen.blit(images_bsv.clipboard[1], (1155, 236))
                if click:
                    data_gen.copy_to_clip(adres)
                    click_wav.play()

        if qr_main:
            qr = images_bsv.qr_codex()
            screen.blit(qr, (1075, 50))

        pygame.display.update()
        mainClock.tick(30)


def open_bsvpl():

    webbrowser.open("https://www.bitcoinsv.pl/")


def open_discord():

    webbrowser.open("https://discord.gg/MkZ9EJa")


def open_yt():

    webbrowser.open("https://www.youtube.com/channel/UCiz2_xk3-uEr8-Taj5G_5qg")


def open_forum():

    webbrowser.open("https://www.forum.bitcoinsv.pl/")


def open_tdxp():

    webbrowser.open("https://tdxp.app/index")



def open_version():

    webbrowser.open("https://www.bitcoinsv.pl/blog/2021/05/14/hubsv-polska-aplikacja-na-blockchain-bitcoin-sv/")


def game_Lynez():
    saldo_main = None
    gotowa_lista = None
    status_woc = woc_api.test_conn()
    numer_notowania, adres_tablicy = lynez_conf.notowanie_lynez()
    if status_woc == 200:
        adres = data_gen.open_address()
        saldo_main = woc_api.saldo(adres)
        saldo_notowania = woc_api.saldo(adres_tablicy)
        wygrana = saldo_notowania[1] * 0.8
        wygrana = round(wygrana, 8)
        suma_notowa = "$ W puli nagród jest: " + str(wygrana) + " BSV"
        lista_wynikow = lynez_conf.address_history_game(adres_tablicy)
        if lista_wynikow:
            ni_wyniki = lynez_conf.unpack_game_list(lista_wynikow)
            gotowa_lista = lynez_conf.delist_game(ni_wyniki)
    game_lyn.play(-1)
    global game_score

    game_text_loc = - 120
    end_text_loc = -220
    transition = 30
    screen_shake = 0
    end_game = False
    player_pos = [display.get_width() // 2, display.get_height() // 2]
    scroll = 0
    last_place = 50
    game_score = 0
    lasers = []
    line_effects = []
    sparks = []
    circle_effects = []
    player_path = []
    bounce_cooldown = 0
    square_effects = []
    particles = []
    player_velocity = [0, 0]
    last_point = [display.get_width() // 2, display.get_height()]
    platforms = [[[0, display.get_height() - 1], [display.get_width(), display.get_height() - 1]]]
    # Loop ------------------------------------------------------- #
    while True:
        click = False

        # Background --------------------------------------------- #
        if transition > 0:
            transition -= 1

        if screen_shake > 0:
            screen_shake -= 1

        if not end_game:
            line_color = (255, 153, 0)
            if player_pos[1] - 200 < scroll:
                scroll += (player_pos[1] - 200 - scroll) / 10
        else:
            line_color = (190, 197, 208)

        if (-scroll) - last_place > 50:
            if random.randint(1, 3) <= 2:
                base_y = scroll - 80
                base_x = random.randint(0, display.get_width())
                new_line = [[base_x, base_y], [base_x + random.randint(0, 200) - 100, base_y + random.randint(0, 100) - 50]]
                if dis_func((new_line[1][0] - new_line[0][0], new_line[1][1] - new_line[0][1])) > 30:
                    new_line.sort()
                    platforms.append(new_line)
            last_place += 50

        game_score = max(game_score, -(player_pos[1] - display.get_height() // 2))

        display.fill((background_color))
        gui_display.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()
        mx -= BORDER_WIDTH
        mx = mx // 2
        my = my // 2

        player_gravity = 0.05 + game_score / 30000
        player_terminal_velocity = 1 + game_score / 3000
        bounce_strength = 1 + game_score / 8000

        if end_game:
            scroll += (- scroll) / 100

        # Square Effects ----------------------------------------- #
        if random.randint(1, 60) == 1:
            square_effects.append([[random.randint(0, display.get_width()), -80 + scroll], random.randint(0, 359), random.randint(10, 30) / 20, random.randint(15, 40), random.randint(10, 30) / 500])

        for i, effect in sorted(enumerate(square_effects), reverse=True): # loc, rot, speed, size, decay
            effect[0][1] += effect[2]
            effect[1] += effect[2] * effect[4]
            effect[3] -= effect[4]
            points = [
                advance(effect[0], math.degrees(effect[1]), effect[3]),
                advance(effect[0], math.degrees(effect[1]) + 90, effect[3]),
                advance(effect[0], math.degrees(effect[1]) + 180, effect[3]),
                advance(effect[0], math.degrees(effect[1]) + 270, effect[3]),
            ]
            points = [[v[0], v[1] - scroll] for v in points]
            if effect[3] < 1:
                square_effects.pop(i)
            else:
                pygame.draw.polygon(display, background_polygon_color, points, 2)

        # Line Effects ------------------------------------------- #
        for i, effect in sorted(enumerate(line_effects), reverse=True): # locs, targets, color, speed, dur
            if len(effect) == 5:
                effect.append(effect[4])
            effect[0][0][0] += (effect[1][0][0] - effect[0][0][0]) / effect[3]
            effect[0][0][1] += (effect[1][0][1] - effect[0][0][1]) / effect[3]
            effect[0][1][0] += (effect[1][1][0] - effect[0][1][0]) / effect[3]
            effect[0][1][1] += (effect[1][1][1] - effect[0][1][1]) / effect[3]
            effect[4] -= 1
            if effect[4] <= 0:
                line_effects.pop(i)
            opacity = 255 * (effect[4] / effect[5])
            color = (effect[2][0], effect[2][1], effect[2][2], opacity)
            #print(effect[0][0], effect[0][1])
            alpha_line(display, color, effect[0][0], effect[0][1])
            #pygame.draw.line(display, effect[2], effect[0][0], effect[0][1])

        # Circle Effects ----------------------------------------- #
        for i, circle in sorted(enumerate(circle_effects), reverse=True): # loc, radius, border_stats, speed_stats, color
            circle[1] += circle[3][0]
            circle[2][0] -= circle[2][1]
            circle[3][0] -= circle[3][1]
            if circle[2][0] < 1:
                circle_effects.pop(i)
            else:
                pygame.draw.circle(display, circle[4], [int(circle[0][0]), int(circle[0][1] - scroll)], int(circle[1]), int(circle[2][0]))

        # Sparks ------------------------------------------------- #
        for i, spark in sorted(enumerate(sparks), reverse=True): # loc, dir, scale, speed
            speed = spark[3]
            scale = spark[2]
            points = [
                advance(spark[0], spark[1], 2 * speed * scale),
                advance(spark[0], spark[1] + 90, 0.3 * speed * scale),
                advance(spark[0], spark[1], -1 * speed * scale),
                advance(spark[0], spark[1] - 90, 0.3 * speed * scale),
            ]
            points = [[v[0], v[1] - scroll] for v in points]
            color = (191, 0, 255)
            if len(spark) > 4:
                color = spark[4]
            pygame.draw.polygon(display, color, points)
            spark[0] = advance(spark[0], spark[1], speed)
            spark[3] -= 0.5
            if spark[3] <= 0:
                sparks.pop(i)

        # Render Drawing Line ------------------------------------ #
        if not end_game:
            pygame.draw.line(display, line_placing_color, [last_point[0], last_point[1] - scroll], [mx, my])
        #if random.randint(1, 10) == 1:
        #    line_effects.append([[[0, 200], [200, 200]], [[50, 100], [150, 100]], (255, 0, 0), 50, 30])
        #    print('boop')

        player_path = player_path[-50:]
        if len(player_path) > 2:
            player_path_mod = [[v[0], v[1] - scroll] for v in player_path]
            pygame.draw.lines(display, line_placing_color, False, player_path_mod)

        # Lasers ------------------------------------------------- #
        if game_score > 300:
            if random.randint(1, 300 * (1 + len(lasers) * 2)) == 1:
                lasers.append([random.randint(0, display.get_width()), random.randint(90, 150), 20])
        for i, laser in sorted(enumerate(lasers), reverse=True):
            left = laser[0] - laser[1] // 2
            if left < 0:
                left = 0
            right = laser[0] + laser[1] // 2
            if right > display.get_width():
                right = display.get_width()
            pygame.draw.line(display, (190, 40, 100), (left, 0), (left, display.get_height()))
            pygame.draw.line(display, (190, 40, 100), (right, 0), (right, display.get_height()))
            center_line = [[laser[0], 0], [laser[0], display.get_height()]]
            if laser[2] % 12 == 0:
                laser_charge_s.play()
                line_effects.append([[[left, 0], [left, display.get_height()]], center_line, (190, 40, 100), 20, 30])
                line_effects.append([[[right, 0], [right, display.get_height()]], center_line, (190, 40, 100), 20, 30])
            laser[2] += 1
            if laser[2] > 180:
                lasers.pop(i)
                laser_explode_s.play()
                if (player_pos[0] > left) and (player_pos[0] < right):
                    if player_pos[0] > laser[0]:
                        player_velocity[0] += 4
                    else:
                        player_velocity[0] -= 4
                    for i in range(30):
                        sparks.append([player_pos, random.randint(0, 359), random.randint(7, 10) / 10 * 3, 9 * random.randint(5, 10) / 10, (170, 170, 170)])
                        a = random.randint(0, 359)
                        s = random.randint(20, 50) / 10
                        x_p = math.cos(math.radians(a)) * s
                        y_p = math.sin(math.radians(a)) * s
                        particles.append(e.particle(player_pos, 'p', [x_p, y_p], 0.1, random.randint(0, 20) / 10, (170, 170, 170)))
                        screen_shake = 8
                for i in range(300):
                    if random.randint(1, 2) == 1:
                        pos_x = left
                        vel = [4 + random.randint(0, 20) / 10, random.randint(0, 10) / 10 - 3]
                    else:
                        pos_x = right
                        vel = [-(4 + random.randint(0, 20) / 10), random.randint(0, 10) / 10 - 3]
                    pos_y = random.randint(0, display.get_height() + 30) + scroll - 30
                    particles.append(e.particle([pos_x, pos_y], 'p', vel, 0.2, random.randint(0, 20) / 10, (160, 40, 80)))

        # Render Platforms --------------------------------------- #
        for platform in platforms:
            if (min(platform[0][1], platform[1][1]) < scroll + display.get_height() + 20) and (max(platform[0][1], platform[1][1]) > scroll - 20):
                pygame.draw.line(display, line_color, [platform[0][0], platform[0][1] - scroll], [platform[1][0], platform[1][1] - scroll], line_width)
                pygame.draw.circle(display, line_color, [platform[0][0], platform[0][1] - scroll], 6, 2)
                pygame.draw.circle(display, line_color, [platform[1][0], platform[1][1] - scroll], 6, 2)
                if random.randint(0, 10) == 0:
                    color = random.randint(150, 220)
                    sparks.append([random.choice(platform), random.randint(0, 359), random.randint(7, 10) / 10, 5 * random.randint(5, 10) / 10, (color, color, color)])

        # Player ------------------------------------------------- #
        particles.append(e.particle(player_pos, 'p', [random.randint(0, 20) / 40 - 0.25, random.randint(0, 10) / 15 - 1], 0.2, random.randint(0, 30) / 10, player_color))
        line_locations = check_line_sides(platforms, player_pos)

        start_pos = player_pos.copy()

        player_velocity[1] = min(player_terminal_velocity, player_velocity[1] + player_gravity)
        player_pos[0] += player_velocity[0]
        player_pos[1] += player_velocity[1]
        player_velocity[1] = normalize(player_velocity[1], 0.02)

        player_path.append(player_pos.copy())

        if bounce_cooldown > 0:
            bounce_cooldown -= 1

        line_locations_post = check_line_sides(platforms, player_pos)
        for i, side in enumerate(line_locations):
            if sign(side) != sign(line_locations_post[i]):
                if sign(side) == -1:
                    if line_math.doIntersect([start_pos, player_pos], platforms[i]):
                        if (player_pos[0] < display.get_width()) and (player_pos[0] > 0):
                            if bounce_cooldown == 0:
                                bounce_s.play()
                                angle = math.atan2(platforms[i][1][1] - platforms[i][0][1], platforms[i][1][0] - platforms[i][0][0])
                                normal = angle - math.pi * 0.5
                                bounce_angle = math.radians(mirror_angle(math.degrees(math.atan2(-player_velocity[1], -player_velocity[0])), math.degrees(normal)) % 360)
                                player_velocity[0] = math.cos(bounce_angle) * (dis_func(player_velocity) + 1)
                                player_velocity[1] = math.sin(bounce_angle) * (dis_func(player_velocity) + 1)
                                player_velocity[1] -= 2 * bounce_strength
                                for i in range(random.randint(4, 6)):
                                    spark_angle = math.degrees(normal) + random.randint(0, 180) - 90
                                    sparks.append([player_pos.copy(), spark_angle, (dis_func(player_velocity) + 1) / 3 * random.randint(7, 10) / 10, (dis_func(player_velocity) + 1) * 2 * random.randint(5, 10) / 10])
                                bounce_cooldown = 3

        if (player_pos[0] < 0) or (player_pos[0] > display.get_width()):
            if end_game == False:
                death_s.play()
                circle_effects.append([player_pos, 6, [6, 0.15], [10, 0.2], (255, 153, 0)])
                circle_effects.append([player_pos, 6, [6, 0.05], [5, 0.04], (190, 40, 100)])
                screen_shake = 12
            end_game = True

        # Particles ---------------------------------------------- #
        for i, particle in sorted(enumerate(particles), reverse=True):
            alive = particle.update(1)
            if not alive:
                particles.pop(i)
            else:
                particle.draw(display, [0, scroll])

        # GUI ---------------------------------------------------- #
        font.render('punkty: ' + str(int(game_score)), gui_display, (game_text_loc, 4))
        font2.render(str(int(game_score)), gui_display, (display.get_width() // 2 - font.width(str(int(game_score))) // 2, end_text_loc + 4))
        font2.render('start R', gui_display, (display.get_width() // 2 - font.width('start R') // 2, end_text_loc + 28))
        font.render(str(int(game_score)), gui_display, (display.get_width() // 2 - font.width(str(int(game_score))) // 2, end_text_loc))
        font.render('start R', gui_display, (display.get_width() // 2 - font.width('start R') // 2, end_text_loc + 24))

        if end_game:
            game_text_loc += (-120 - game_text_loc) / 20
            end_text_loc += (200 - end_text_loc) / 20
        else:
            game_text_loc += (6 - game_text_loc) / 10
            end_text_loc += (-220 - end_text_loc) / 20

        # Buttons ------------------------------------------------ #
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_r:
                    if end_game:
                        restart_s.play()
                        transition = 30
                        lasers = []
                        line_effects = []
                        sparks = []
                        player_path = []
                        game_score = 0
                        end_game = False
                        particles = []
                        platforms = [[[0, display.get_height() - 1], [display.get_width(), display.get_height() - 1]]]
                        last_point = [display.get_width() // 2, display.get_height()]
                        scroll = 0
                        player_pos = [display.get_width() // 2, display.get_height() // 2]
                        player_velocity = [0, 0]
                        circle_effects = []
                        last_place = 50
                        square_effects = []
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    if not end_game:
                        line = [last_point, [mx, my + scroll]]
                        line.sort()
                        platforms.append(line)
                        last_point = [mx, my + scroll]
                        circle_effects.append([[mx, my + scroll], 4, [4, 0.2], [4, 0.3], (255, 255, 255)])
                        place_s.play()

        # Update ------------------------------------------------- #
        display_background = display.copy()
        display_background.set_alpha(25) # background opacity
        black_surf = pygame.Surface(screen.get_size())
        black_surf.fill(background_color)
        black_surf.set_alpha(85) # blur
        display.set_colorkey((background_color))
        screen.blit(pygame.transform.scale(display_background, (display.get_width() * 2 + 40, display.get_height() * 2 + 40)), (-20 + BORDER_WIDTH, 0))
        screen.blit(black_surf,(0, 0))
        offset = [0, 0]
        if screen_shake:
            offset[0] += random.randint(0, 10) - 5
            offset[1] += random.randint(0, 10) - 5
        screen.blit(pygame.transform.scale(display, (display.get_width() * 2, display.get_height() * 2)), (BORDER_WIDTH + offset[0], offset[1]))
        screen.blit(pygame.transform.scale(gui_display, (display.get_width() * 2, display.get_height() * 2)),(BORDER_WIDTH, 0))
        border_box = pygame.Rect(0, 0, BORDER_WIDTH, screen.get_height())
        pygame.draw.rect(screen, (0, 0, 0), border_box)
        border_box.x = screen.get_width() - BORDER_WIDTH
        pygame.draw.rect(screen, (0, 0, 0), border_box)
        if transition:
            black_surf = pygame.Surface(screen.get_size())
            black_surf.set_alpha(255 * transition / 30)
            screen.blit(black_surf, (0, 0))

        screen.blit(images_bsv.black, (622, 0))
        exit_0 = screen.blit(images_bsv.exit_game, (400, 0))
        if exit_0.collidepoint((mx, my)):
            woc_api.test_text("tytul_1", ">>         <<", 913, 50, red, 20)
            if click:
                game_lyn.stop()
                main_intro.play()
                click_wav.play()
                break

        if not numer_notowania and adres_tablicy:
            woc_api.test_text("1", "Rywalizacja zakończona.", 882, 252, white, 16)
            woc_api.test_text("1", "Oczekuj kolejnego notowania.", 852, 272, white, 16)
        else:
            if game_score > 0 and saldo_main[1] > 0.0006:
                screen.blit(images_bsv.add_point[0], (1200, 110))
                append_0 = screen.blit(images_bsv.exit_game, (560, 50))
                if append_0.collidepoint((mx, my)):
                    woc_api.test_text("tytul1", "+      + ", 1180, 126, green, 20)
                    if click:
                        lynez_conf.window_lynez_game(adres_tablicy, str(game_score))
                        # tu dodać adres konkursowy

            woc_api.test_text("tytul", "  Najlepsze wyniki", 872, 179, white, 20)
            woc_api.test_text("tytul1", "*Lynez Game*", 250, 10, white, 20)
            woc_api.test_text("tytul71", "*Twój wynik : ", 760, 125, white, 20)
            woc_api.test_text("tytul2", str(game_score), 940, 125, white, 20)
            if gotowa_lista:
                if len(gotowa_lista) >= 1:
                    screen.blit(images_bsv.trophy[0], (800, 222))
                    nazwa_gr = gotowa_lista[0][1]
                    miejsce_1 = " " + nazwa_gr[:10] + " : " + str(gotowa_lista[0][0])
                    woc_api.test_text("1", miejsce_1, 822, 222, gold, 20)

                if len(gotowa_lista) >= 2:
                    screen.blit(images_bsv.trophy[1], (800, 252))
                    nazwa_gr = gotowa_lista[1][1]
                    miejsce_2 = " " + nazwa_gr[:10] + " : " + str(gotowa_lista[1][0])
                    woc_api.test_text("1", miejsce_2, 822, 252, white, 20)

                if len(gotowa_lista) >= 3:
                    screen.blit(images_bsv.trophy[2], (800, 282))
                    nazwa_gr = gotowa_lista[2][1]
                    miejsce_3 = " " + nazwa_gr[:10] + " : " + str(gotowa_lista[2][0])
                    woc_api.test_text("1", miejsce_3, 822, 282, bronze, 20)

                if len(gotowa_lista) >= 4:
                    nazwa_gr = gotowa_lista[3][1]
                    miejsce_4 = "4." + nazwa_gr[:10] + " : " + str(gotowa_lista[3][0])
                    woc_api.test_text("1", miejsce_4, 822, 312, grey, 18)

                if len(gotowa_lista) >= 5:
                    nazwa_gr = gotowa_lista[4][1]
                    miejsce_5 = "5." + nazwa_gr[:10] + " : " + str(gotowa_lista[4][0])
                    woc_api.test_text("1", miejsce_5, 822, 342, grey, 18)

                if len(gotowa_lista) >= 6:
                    nazwa_gr = gotowa_lista[5][1]
                    miejsce_6 = "6." + nazwa_gr[:10] + " : " + str(gotowa_lista[5][0])
                    woc_api.test_text("1", miejsce_6, 822, 372, grey, 18)

                if len(gotowa_lista) >= 7:
                    nazwa_gr = gotowa_lista[6][1]
                    miejsce_7 = "7." + nazwa_gr[:10] + " : " + str(gotowa_lista[6][0])
                    woc_api.test_text("1", miejsce_7, 822, 402, grey, 18)

                if len(gotowa_lista) >= 8:
                    nazwa_gr = gotowa_lista[7][1]
                    miejsce_8 = "8." + nazwa_gr[:10] + " : " + str(gotowa_lista[7][0])
                    woc_api.test_text("1", miejsce_8, 822, 432, grey, 18)

                if len(gotowa_lista) >= 9:
                    nazwa_gr = gotowa_lista[8][1]
                    miejsce_9 = "9." + nazwa_gr[:10] + " : " + str(gotowa_lista[8][0])
                    woc_api.test_text("1", miejsce_9, 822, 462, grey, 18)

                if len(gotowa_lista) >= 10:
                    nazwa_gr = gotowa_lista[9][1]
                    miejsce_10 = "10." + nazwa_gr[:10] + " : " + str(gotowa_lista[9][0])
                    woc_api.test_text("1", miejsce_10, 822, 492, grey, 18)
            else:
                woc_api.test_text("1", "Brak wyników", 922, 222, gold, 20)

            woc_api.test_text("1", suma_notowa, 802, 542, green, 18)

        pygame.display.update()
        mainClock.tick(45)


def papier():
    running = True
    wyborek = None
    ai_choice = None
    gotowa_lista = None
    play = 1
    punkty = 0
    pkn_wav.play(-1)
    status_woc = woc_api.test_conn()
    numer_notowania, adres_tablicy = pkn_conf.notowanie_pkn()
    x_c = 55
    if status_woc == 200:
        adres = data_gen.open_address()
        saldo_main = woc_api.saldo(adres) # <--- dokończyć
        lista_wynikow = lynez_conf.address_history_game(adres_tablicy)
        if lista_wynikow:
            ni_wyniki = lynez_conf.unpack_game_list(lista_wynikow)
            gotowa_lista = lynez_conf.delist_game(ni_wyniki)
    while running:
        click = False

        screen.fill(black)
        screen.blit(images_bsv.pakano_bg, (0, 0))
        screen.blit(images_bsv.glass_tv, (385, 160))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if not txid:
            pkn_wav.stop()
            main_intro.play(-1)
            break
        papierek = screen.blit(images_bsv.papier_wybor, (120, 100))
        nozyk = screen.blit(images_bsv.noz_wybor, (120, 500))
        kamyk = screen.blit(images_bsv.kamien_wybor, (120, 300))
        back_0 = screen.blit(images_bsv.back[0], (40, 650))

        if back_0.collidepoint((mx, my)):
            screen.blit(images_bsv.back[1], (40, 650))
            if click:
                pkn_wav.stop()
                main_intro.play()
                click_wav.play()
                break

        if play == 1:
            if papierek.collidepoint((mx, my)):
                screen.blit(images_bsv.papier_wybor1, (120, 100))
                if click:
                    win.play()
                    wyborek = "papier_gracz"
            if kamyk.collidepoint((mx, my)):
                screen.blit(images_bsv.kamien_wybor1, (120, 300))
                if click:
                    win.play()
                    wyborek = "kamien_gracz"
            if nozyk.collidepoint((mx, my)):
                screen.blit(images_bsv.noz_wybor1, (120, 500))
                if click:
                    win.play()
                    wyborek = "nozyce_gracz"

        # PC
        if ai_choice == None:
            screen.blit(images_bsv.wybor_pc, (720, 300))
        elif ai_choice == "papier_pc":
            screen.blit(images_bsv.papier_wybor, (720, 300))
        elif ai_choice == "kamien_pc":
            screen.blit(images_bsv.kamien_wybor, (720, 300))
        elif ai_choice == "nozyce_pc":
            screen.blit(images_bsv.noz_wybor, (720, 300))

        # Player
        if wyborek == "papier_gracz":
            screen.blit(images_bsv.papier_wybor, (460, 300))
        elif wyborek == "kamien_gracz":
            screen.blit(images_bsv.kamien_wybor, (460, 300))
        elif wyborek == "nozyce_gracz":
            screen.blit(images_bsv.noz_wybor, (460, 300))

        if wyborek != None and play == 1:
            start_pkn = screen.blit(images_bsv.graj_pkn[0], (600, 560))
            if start_pkn.collidepoint((mx, my)):
                screen.blit(images_bsv.graj_pkn[1], (600, 560))
                if click:
                    ai_choice = losowanie()

        # Remisy
        if wyborek == "papier_gracz" and ai_choice == "papier_pc":
            play = 0
            screen.blit(images_bsv.remis, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    ai_choice = None
                    wyborek = None
                    play = 1
        if wyborek == "kamien_gracz" and ai_choice == "kamien_pc":
            play = 0
            screen.blit(images_bsv.remis, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    ai_choice = None
                    wyborek = None
                    play = 1
        if wyborek == "nozyce_gracz" and ai_choice == "nozyce_pc":
            play = 0
            screen.blit(images_bsv.remis, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    ai_choice = None
                    wyborek = None
                    play = 1
        # Wygrane
        if wyborek == "papier_gracz" and ai_choice == "kamien_pc":
            play = 0
            screen.blit(images_bsv.trophy_pkm, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    punkty += 1
                    ai_choice = None
                    wyborek = None
                    play = 1
        if wyborek == "kamien_gracz" and ai_choice == "nozyce_pc":
            play = 0
            screen.blit(images_bsv.trophy_pkm, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    punkty += 1
                    ai_choice = None
                    wyborek = None
                    play = 1
        if wyborek == "nozyce_gracz" and ai_choice == "papier_pc":
            play = 0
            screen.blit(images_bsv.trophy_pkm, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    punkty += 1
                    ai_choice = None
                    wyborek = None
                    play = 1
        # Przegrane
        if wyborek == "nozyce_gracz" and ai_choice == "kamien_pc":
            play = 0
            screen.blit(images_bsv.dead, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    punkty = 0
                    ai_choice = None
                    wyborek = None
                    play = 1
        if wyborek == "kamien_gracz" and ai_choice == "papier_pc":
            play = 0
            screen.blit(images_bsv.dead, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    punkty = 0
                    ai_choice = None
                    wyborek = None
                    play = 1
        if wyborek == "papier_gracz" and ai_choice == "nozyce_pc":
            play = 0
            screen.blit(images_bsv.dead, (600, 200))
            resecik = screen.blit(images_bsv.reset[0], (610, 650))
            if resecik.collidepoint((mx, my)):
                screen.blit(images_bsv.reset[1], (610, 650))
                if click:
                    punkty = 0
                    ai_choice = None
                    wyborek = None
                    play = 1

        if not numer_notowania and adres_tablicy:
            woc_api.test_text("1", "Rywalizacja zakończona.", 882, 252, white, 16)
            woc_api.test_text("1", "Oczekuj kolejnego notowania.", 852, 272, white, 16)
        else:
            if punkty > 0 and play == 1 and saldo_main[1] > 0.0006:
                pygame.draw.circle(screen, (0, 153, 51), (910, 65), x_c, 1)
                x_c += 1
                if x_c == 70:
                    x_c = 55
                set_point_0 =  screen.blit(images_bsv.set_point[0], (860, 20))
                if set_point_0.collidepoint((mx, my)):
                    screen.blit(images_bsv.set_point[1], (860, 20))
                    if click:
                        pkn_conf.window_pkn_game(adres_tablicy, str(punkty))

            if gotowa_lista:
                if len(gotowa_lista) >= 1:
                    screen.blit(images_bsv.trophy[0], (990, 422))
                    nazwa_gr = gotowa_lista[0][1]
                    miejsce_1 = " " + nazwa_gr[:10] + " : " + str(gotowa_lista[0][0])
                    woc_api.test_text("1", miejsce_1, 1012, 422, gold, 16)

                if len(gotowa_lista) >= 2:
                    screen.blit(images_bsv.trophy[1], (990, 452))
                    nazwa_gr = gotowa_lista[1][1]
                    miejsce_2 = " " + nazwa_gr[:10] + " : " + str(gotowa_lista[1][0])
                    woc_api.test_text("1", miejsce_2, 1012, 452, white, 16)

                if len(gotowa_lista) >= 3:
                    screen.blit(images_bsv.trophy[2], (990, 482))
                    nazwa_gr = gotowa_lista[2][1]
                    miejsce_3 = " " + nazwa_gr[:10] + " : " + str(gotowa_lista[2][0])
                    woc_api.test_text("1", miejsce_3, 1012, 482, bronze, 16)

                if len(gotowa_lista) >= 4:
                    nazwa_gr = gotowa_lista[3][1]
                    miejsce_4 = "4." + nazwa_gr[:10] + " : " + str(gotowa_lista[3][0])
                    woc_api.test_text("1", miejsce_4, 1012, 512, (125, 102, 78), 14)

                if len(gotowa_lista) >= 5:
                    nazwa_gr = gotowa_lista[4][1]
                    miejsce_5 = "5." + nazwa_gr[:10] + " : " + str(gotowa_lista[4][0])
                    woc_api.test_text("1", miejsce_5, 1012, 542, grey, 14)

                if len(gotowa_lista) >= 6:
                    nazwa_gr = gotowa_lista[5][1]
                    miejsce_6 = "6." + nazwa_gr[:10] + " : " + str(gotowa_lista[5][0])
                    woc_api.test_text("1", miejsce_6, 1012, 572, (89, 89, 89), 14)

                if len(gotowa_lista) >= 7:
                    nazwa_gr = gotowa_lista[6][1]
                    miejsce_7 = "7." + nazwa_gr[:10] + " : " + str(gotowa_lista[6][0])
                    woc_api.test_text("1", miejsce_7, 1012, 602, (64, 64, 64), 14)

                if len(gotowa_lista) >= 8:
                    nazwa_gr = gotowa_lista[7][1]
                    miejsce_8 = "8." + nazwa_gr[:10] + " : " + str(gotowa_lista[7][0])
                    woc_api.test_text("1", miejsce_8, 1012, 632, (51, 51, 51), 14)
            else:
                woc_api.test_text("1", "Brak wyników.", 1027, 422, gold, 16)


        particlesZ.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 5)])
        for particle in particlesZ:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.05
            particle[1][1] += 0.1
            pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particlesZ.remove(particle)

        woc_api.test_text("tytul6", "Punkty: " + str(punkty), 357, 100, white, 30)
        screen.blit(images_bsv.glass_tv, (385, 160))
        pygame.display.update()
        mainClock.tick(30)

def losowanie():

    krotka_pc = ("papier_pc", "kamien_pc", "nozyce_pc")
    wybor_ai = random.randint(0,2)
    return krotka_pc[wybor_ai]

def check_line_sides(lines, point):
    line_status = []
    for line in lines:
        line_status.append((line[1][0] - line[0][0]) * (point[1] - line[0][1]) - (line[1][1] - line[0][1]) * (point[0] - line[0][0]))
    return line_status

def sign(num):
    if num != 0:
        return num / abs(num)
    else:
        return 1

def mirror_angle(original,base):
    dif = 180-base
    base = 180
    new = original+dif
    new = new % 360
    dif = base-new
    return original + dif * 2

def dis_func(dis):
    return math.sqrt(dis[0] ** 2 + dis[1] ** 2)


def no_data_site():
    pygame.mixer.music.play()
    global user_text
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(images_bsv.bg_black, (0, 0))

        about_lbl = screen.blit(images_bsv.about[0], (25, 590))
        if about_lbl.collidepoint((mx, my)):
            screen.blit(images_bsv.about[1], (25, 590))
            if click:
                open_version()

        text_surface = myFont.render(user_text, True, white)
        screen.blit(text_surface, (440, 380))
        if len(user_text) > 8:
            ok_lbl = screen.blit(images_bsv.ok_button[0], (870, 350))
            if ok_lbl.collidepoint((mx, my)):
                screen.blit(images_bsv.ok_button[1], (870, 350))
                if click:
                    data_gen.verify_hash(user_text)
                    check_files = data_gen.check_dat()
                    if check_files:
                        click_wav.play()
                        data_site()

        pygame.display.update()
        mainClock.tick(30)


def data_site():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)
        screen.blit(images_bsv.bg_white, (0, 0))
        pygame.display.update()
        mainClock.tick(30)


#  Uruchomienie głównego okna
check_file = data_gen.check_dat()
if not check_file:
    no_data_site()
else:
    hubsv_menu(hub_ver)
